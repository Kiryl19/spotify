from django.db import models


DEFAULT_IMAGE = ''


class Genre(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='images/genres')


class Artist(models.Model):
    name = models.CharField(max_length=200)
    genres = models.ManyToManyField(Genre, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='images/artists', default=DEFAULT_IMAGE)


class Song(models.Model):

    def get_default_image(self):
        if self.album:
            return self.album.image
        else:
            return DEFAULT_IMAGE

    song = models.CharField(max_length=200)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    album = models.ForeignKey('Album', on_delete=models.SET_NULL,
                              blank=True, null=True)
    release_date = models.DateField(auto_now_add=True)
    genres = models.ManyToManyField(Genre, blank=True, null=True)
    image = models.ImageField(upload_to='images/songs', default=get_default_image)
    text = models.TextField(blank=True, null=True)


class Album(models.Model):
    name = models.CharField(max_length=200)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    genres = models.ManyToManyField(Genre, blank=True, null=True)
    release_date = models.DateField(auto_now_add=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='images/albums', default=DEFAULT_IMAGE)


class UserPlaylist(models.Model):
    name = models.CharField(verbose_name='Название плейлиста', max_length=250)
    profile = models.ForeignKey('authorization.Profile', on_delete=models.CASCADE,
                                blank=True, null=True)


class PublicPlaylist(models.Model):
    name = models.CharField(verbose_name='Название плейлиста', max_length=250)
    profile = models.ManyToManyField('authorization.Profile', blank=True, null=True)
    image = models.ImageField(upload_to='images/public_playlists', default=DEFAULT_IMAGE)
