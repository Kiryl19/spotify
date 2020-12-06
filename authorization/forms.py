from django import forms

class RegistrationForm(forms.Form):
    username = forms.CharField(label='Логин', max_length=40)
    password = forms.CharField(label='Пароль', max_length=128)
    password2 = forms.CharField(label='Повторите пароль', max_length=128)
    email = forms.EmailField(label='Email', max_length=40)


class ProfileForm(forms.Form):
    firstname = forms.CharField(label='Имя', max_length=40)
    lastname = forms.CharField(label='Фамилия', max_length=40)
    birthday = forms.DateField(label='День рождения')
    image = forms.FileField(label='Фото профиля')

class LoginForm(forms.Form):
    username_or_login = forms.CharField(label='Логин или пароль', max_length=40)
    password = forms.CharField(max_length=128)
