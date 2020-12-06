from django import forms

class UserPlaylistForm(forms.Form):
    name = forms.CharField(verbose_name='Название плейлиста', max_length=250)