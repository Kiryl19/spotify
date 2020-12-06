from django.urls import path
from . import views

urlpatterns = [path('crateplaylist/', views.PlaylistCreateView.as_view(), name='crateplaylist'),
               path('listpublicplaylist/', views.listpublicplaylist, name='listpublicplaylist'),
               path('listuserplaylist/', views.listuserplaylist, name='listuserplaylist'),
               path('listalbum/', views.listalbum, name='listalbum')
]