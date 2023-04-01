from django.shortcuts import render
from AppEntrega.models import Song, Artist, Musical
from AppEntrega.forms import SongForm,ArtistForm,MusicalForm,SearchSongForm
from django.views.generic import ListView


def welcome(request):
    return render(request,"AppEntrega/index.html")

def song_create(request):
    form = SongForm(request.POST)
    context = {"form": form}

    if form.is_valid():
        song = Song(song=form.cleaned_data["song"], duration=form.cleaned_data["duration"], musical=form.cleaned_data["musical"])
        song.save()
        context["form"] = SongForm()

    context["songs"] = Song.objects.all()
    context["total_songs"] = len(Song.objects.all())
    return render(request, "AppEntrega/canciones.html", context)


def artist_create(request):
    form = ArtistForm(request.POST)
    context = {"form": form}

    if form.is_valid():
        artist = Artist(name=form.cleaned_data["name"], surname=form.cleaned_data["surname"], musical=form.cleaned_data["musical"], date_of_birth=form.cleaned_data["date_of_birth"])
        artist.save()
        context["form"] = ArtistForm()

    artists = Artist.objects.all()
    context["artists"] = artists
    context['total_artists'] = len(artists)
    return render(request, "AppEntrega/artistas.html", context)


def musical_create(request):
    form = MusicalForm(request.POST)
    context = {"form": form}

    if form.is_valid():
        musical = Musical(musical=form.cleaned_data["musical"], year_of_opening=form.cleaned_data["year_of_opening"])
        musical.save()
        context["form"] = MusicalForm()

    context["musicals"] = Musical.objects.all()
    context["total_musicals"] = Musical.objects.count()
    return render(request, "AppEntrega/musicales.html", context)


class search(ListView):
    model = Song
    context_object_name = "songs"

    def get_queryset(self):
        f = SearchSongForm(self.request.GET)
        if f.is_valid():
            return Song.objects.filter(song__icontains = f.data["criterio_song"]).all()
        else:
            return Song.objects.none()