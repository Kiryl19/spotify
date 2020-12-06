from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import UserManager


class User(AbstractBaseUser):
    username = models.CharField(max_length=40, unique=True)
    password = models.CharField('password', max_length=128)
    email = models.EmailField(max_length=40, unique=True)
    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'
    objects = UserManager()


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    create_date = models.DateTimeField(auto_now_add=True)
    birthday = models.DateField()
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    songs_liked = models.ManyToManyField('music.Song', blank=True, null=True)
    favourite_genres = models.ManyToManyField('music.Genre', blank=True, null=True)
    favourite_artists = models.ManyToManyField('music.Artist', blank=True, null=True)
