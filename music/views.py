from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from authorization import models as modelsauth
from . import models as modelsmusic
from .forms import UserPlaylistForm


def listuserplaylist(request):
    profile = modelsauth.Profile.objects.get(user=request.user)
    listuserplaylist = modelsmusic.UserPlaylist.objects.filter(profile=profile)
    return render(request, 'listuserplaylist.html', {'listuserplaylist': listuserplaylist})

def listpublicplaylist(request):
    profile = modelsauth.Profile.objects.get(user=request.user)
    listpublicplaylist = modelsmusic.PublicPlaylist.objects.filter(profile=profile)
    return render(request, 'listpublicplaylist.html', {'listpublicplaylist': listpublicplaylist})

def listalbum(request):
    listalbum = modelsmusic.Album.objects.all()
    return render(request, 'listalbum.html', {'listalbum': listalbum})

class PlaylistCreateView(TemplateView):
    template_name = 'music/crateplaylist.html'

    def get_context_data(self, **kwargs):
        user_playlist_form = UserPlaylistForm()
        return ({'user_playlist_form': user_playlist_form,
                 })

    def post(self, request):
        user_playlist_form = UserPlaylistForm(request.POST)
        try:
            user_playlist_clean = None
            if user_playlist_form.is_valid():
                user_playlist_clean = user_playlist_form.cleaned_data
            profile = modelsauth.Profile.objects.get(user=request.user)
            user_playlist = modelsmusic.Playlist(profile=profile,
                                                 name=user_playlist_clean['name'])
            user_playlist.save()
        except ValueError:
            return render(request, self.template_name, {'user_playlist_form': user_playlist_form,
                                                        })
        return redirect('/')
