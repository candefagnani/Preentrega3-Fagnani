"""Preentrega3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from AppEntrega.views import song_create,artist_create,musical_create,search,welcome

urlpatterns = [
    path('welcome', welcome, name='welcome'),
    path('song/create/', song_create, name='song_create'),
    path('artist/create/', artist_create, name='artist_create'),
    path('musical/create/', musical_create, name='musical_create'),
    path('search/', search.as_view(), name='song-search'),
    path('admin/', admin.site.urls),
]
