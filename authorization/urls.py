from django.urls import path
from . import views

urlpatterns = [path('registration/', views.RegistrationView.as_view(), name='registration'),
               path('', views.LoginView.as_view(), name='login'),
               path('logout/', views.logout_view, name='logout'),
               path('profile/', views.ProfileView.as_view(), name='profile')


]