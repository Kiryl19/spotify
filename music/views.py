from django.shortcuts import render
from authorization import models as auth_models
from . import models as music_models


def list_all_songs_in_playlist(request, playlist):
    profile = auth_models.Profile.objects.get(user=request.user)
    playlist = music_models.UserPlaylist.objects.get(name=playlist, profile=profile)
    playlist_songs = playlist.songs.all()
    return render(request, 'playlist_detail.html', context={'playlist_songs': playlist_songs,
                  'playlist_name': playlist.name})
