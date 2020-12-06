from django.contrib.auth import logout
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib import auth
from . import models
from .forms import RegistrationForm, ProfileForm, LoginForm


class RegistrationView(TemplateView):
    template_name = 'authorization/registration.html'

    def get_context_data(self, **kwargs):
        user_form = RegistrationForm()
        return ({'user_form': user_form,
                       })

    def post(self, request):
        user_form = RegistrationForm(request.POST, request.FILES)
        try:
            if user_form.is_valid():
                user_clean = user_form.cleaned_data
                if user_clean['password'] == user_clean['password2']:
                    user = models.User(username=user_clean['username'],
                                       email=user_clean['email'],
                                       password=user_clean['username'])
                    user.save()
                    user2 = models.User.objects.get(username=f'{user.username}')
                    if user2 is not None:
                        auth.login(request, user)
                    else:
                        return HttpResponse('Disabled account')
                else:
                    return HttpResponse('Form is not a valid')
        except ValueError:
            return render(request, self.template_name, {'user_form': user_form,

                                                                                     })
        return redirect('/')


class LoginView(TemplateView):
    template_name = 'authorization/login.html'

    def get_context_data(self, **kwargs):
        login_form = LoginForm()
        return ({'login_form': login_form,
                 })

    def post(self, request):
        login_form = LoginForm(request.POST)
        try:
            user = None
            if login_form.is_valid():
                user_clean = login_form.cleaned_data
                user = models.User.objects.get(username=f'{user_clean["username_or_login"]}')
            if user is not None:
                auth.login(request, user)
            else:
                return HttpResponse('Disabled account')
        except ValueError:
            return render(request, self.template_name, {'login_form': login_form,
                                                        })
        return redirect('/')


class ProfileView(TemplateView):
    template_name = 'authorization/profile.html'

    def get_context_data(self, **kwargs):
        profile_form = ProfileForm()
        return ({'profile_form': profile_form,
                 })

    def post(self, request):
        profile_form = ProfileForm(request.POST, request.FILES)
        try:
            profile_clean = None
            if profile_form.is_valid():
                profile_clean = profile_form.cleaned_data
            user = models.User.objects.get(username=request.user.username)
            profile_user = models.Profile(user=user,
                               firstname=profile_clean['firstname'],
                               birthday=profile_clean['birthday'],
                               image=profile_clean['image'])
            profile_user.save()
        except ValueError:
            return render(request, self.template_name, {'profile_form': profile_form,
                                                        })
        return redirect('/')


def logout_view(request):
    logout(request)
    return HttpResponse('Вы вышли')
