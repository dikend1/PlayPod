from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from .serializers import RegisterSerializer,LoginSerializer
import requests
from .models import Track,Album,Favorite,UserProfile
from rest_framework.permissions import IsAuthenticated

DEEZER_API_URL = 'https://api.deezer.com'

@api_view(['GET'])
def get_tracks(request):
    query = request.GET.get('query','rock')
    artist = request.GET.get('artist',None)
    genre = request.GET.get('genre',None)

    deezer_url = f"{DEEZER_API_URL}/search?q={query}"

    if artist:
        deezer_url += f"&artist={artist}"
    if genre:
        deezer_url += f"&genre={genre}"

    response = requests.get(deezer_url)

    if response.status_code == 200:
        data = response.json()
        tracks_data = data['data']
        tracks = []

        for track in tracks_data:
            tracks.append({
                'title': track['title'],
                'artist': track['artist']['name'],
                'genre': track.get('genre','Unknown'),
                'cover_image': track['album']['cover_medium'],
                'audio_url': track['preview'],
                'album': track['album']['title']
            })
        return Response(tracks,status = status.HTTP_200_OK)
    else:
        return Response({
            'error': 'Unable to fetch data from Deezer API'
        },status = status.HTTP_400_BAD_REQUEST)



@api_view(['GET'])
def get_albums(request):
    query = request.GET.get('query','rock')
    artist = request.GET.get('artist',None)
    genre = request.GET.get('genre',None)
    deezer_url = f"{DEEZER_API_URL}/search/album?q={query}"

    if artist:
        deezer_url += f"&artist={artist}"
    if genre:
        deezer_url += f"&genre={genre}"

    response = requests.get(deezer_url)

    if response.status_code == 200:
        data = response.json()
        albums_data = data['data']
        albums = []

        for album in albums_data:
            albums.append({
                'title': album['title'],
                'artist': album['artist']['name'],
                'cover_image':album['cover_medium'],
                'tracks_count': album['nb_tracks']
            })

        return Response(albums,status = status.HTTP_200_OK)
    else:
        return Response({
            'error': 'Unable to fetch data from Deezer API'
        },status = status.HTTP_400_BAD_REQUEST)

current_track = None
is_playing = False

tracks = []
@api_view(['POST'])
def next_track(request):
    global current_track

    try:
        current_track_id = request.data.get('current_track_id')

        current_index = next((index for(index,track) in enumerate(tracks) if track['id'] == current_track_id),None)

        if current_index is None:
            return Response({'error': 'Track not found'},status = status.HTTP_404_NOT_FOUND)

        next_index = (current_index+1)%len(tracks)
        next_track = tracks[next_index]

        current_track = next_track['id']
        return Response({
            'message': 'Track changed',
            'new_track': next_track
        }, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'error': f'Error changing track: {str(e)}'},status = status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['POST'])
def play_track(request):
    global current_track,is_playing
    track_id = request.data.get('track_id')
    try:
        if track_id != current_track:
            current_track = track_id
            is_playing = True
        return Response({'message': 'Track started playing'},status = status.HTTP_200_OK)
    except Exception as e:
        return Response({'error': f'Error playing track: {str(e)}'},status = status.HTTP_500_INTERNAL_SERVER_ERROR)



@api_view(['POST'])
def pause_track(request):
    global is_playing
    is_playing = False
    return Response({'message': 'Track paused'},status = status.HTTP_200_OK)


@api_view(['POST'])
def register_user(request):
    serializer = RegisterSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response({
            'message': 'User created successfully'
        })
    return Response(serializer.data,status = status.HTTP_201_CREATED)

@api_view(['POST'])
def login_user(request):
    serializer = LoginSerializer(data=request.data)

    if serializer.is_valid():
        return Response({
            'message': 'User logged in successfully'
        })
    return Response(serializer.data,status = status.HTTP_201_CREATED)

@api_view(['GET'])
def search(request):
    query = request.GET.get('query','')
    artist = request.GET.get('artist',None)
    genre = request.GET.get('genre',None)
    search_type = request.GET.get('type','track')


    deezer_url = f"{DEEZER_API_URL}/search?q={query}"

    if artist:
        deezer_url += f"&artist={artist}"
    if genre:
        deezer_url += f"&genre={genre}"

    if search_type:
        deezer_url = f"{DEEZER_API_URL}/search/album?q={query}"
        if artist:
            deezer_url += f"&artist={artist}"
        if genre:
            deezer_url += f"&genre={genre}"
    try:
        response = requests.get(deezer_url)
        if response.status_code == 200:
            data = response.json()

            if search_type == 'track':
                tracks_data = data['data']
                tracks = [{
                    'title': track['title'],
                    'artist': track['artist']['name'],
                    'genre': track.get('genre', 'Unknown')
                }for track in tracks_data]
                return Response(tracks,status = status.HTTP_200_OK)

            if search_type == 'album':
                albums_data = data['data']
                albums = [{
                    'title': album['title'],
                    'artist': album[artist]['name']
                }for album in albums_data]
                return Response(albums,status = status.HTTP_200_OK)

            return Response({'error': 'Invalid search type'}, status=status.HTTP_400_BAD_REQUEST)

    except Exception as e:
        return Response({'error': f'Error fetching data from Deezer API: {str(e)}'},status = status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
def add_to_favorites(request):
    track_id = request.data.get('track_id')
    user = request.user

    try:
        track = Track.objects.get(id=track_id)
        favorite, created = Favorite.objects.get_or_create(user=user,track=track)
        if created:
            return Response({'message': 'Track added to favorites'},status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Track is already in favorites'}, status=status.HTTP_400_BAD_REQUEST)
    except Track.DoesNotExist:
        return Response({'error': 'Track not found'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def remove_from_favorites(request):
    track_id = request.data.get('track_id')
    user = request.user
    try:
        track = Track.objects.get(id=track_id)
        favorite = Favorite.objects.get(user=user,track=track)
        favorite.delete()
        return Response({'message': 'Track removed from favorites'},status=status.HTTP_200_OK)
    except Track.DoesNotExist:
        return Response({'error': 'Track not found '}, status=status.HTTP_404_NOT_FOUND)
    except Favorite.DoesNotExist:
        return Response({'error': 'Track is not in favorites'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_favorites(request):
    user = request.user
    if user.is_anonymous:
        return Response({'error': 'User is not authenticated'}, status=status.HTTP_401_UNAUTHORIZED)
    favorites = Favorite.objects.filter(user=user)
    tracks = [{
        'title': fav.track.title,
        'artist': fav.track.artist,
        'cover_image': fav.track.cover_image,
        'audio_url': fav.track.audio_url
    }for fav in favorites]
    return Response(tracks,status = status.HTTP_200_OK)







