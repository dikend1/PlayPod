from tkinter.font import names

from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_user, name='register'),
    path('login/', views.login_user, name='login'),
    path('get_tracks/', views.get_tracks, name='deezer_tracks'),
    path('get_albums/', views.get_albums, name='deezer_albums'),
    path('search/', views.search, name='search'),

    path('add_to_favorites/', views.add_to_favorites, name='add_to_favorites'),
    path('remove_from_favorites/', views.remove_from_favorites, name='remove_from_favorites'),
    path('get_favorites/', views.get_favorites, name='get_favorites'),
]
