from tkinter.font import names

from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_user, name='register'),
    path('api/login/', views.login_user, name='login'),
    path('api/get_tracks/', views.get_tracks, name='deezer_tracks'),
    path('api/get_albums/', views.get_albums, name='deezer_albums'),
    path('api/search/', views.search, name='search'),

    path('api/add_to_favorites/', views.add_to_favorites, name='add_to_favorites'),
    path('api/remove_from_favorites/', views.remove_from_favorites, name='remove_from_favorites'),
    path('api/get_favorites/', views.get_favorites, name='get_favorites'),
    path('api/next_track/', views.next_track, name='next_track'),
]
