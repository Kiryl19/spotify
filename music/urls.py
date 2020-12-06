from django.urls import path
from . import views


urlpatterns = [
    path('playlists/str:playlist_name>', views.list_all_songs_in_playlist, name='playlist_detail')
]
