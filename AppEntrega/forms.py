from django import forms

class MusicalForm(forms.Form):
    musical = forms.CharField(max_length = 100)
    year_of_opening = forms.CharField(max_length= 100)

class SongForm(forms.Form):
    song = forms.CharField(max_length=100)
    duration = forms.CharField(max_length=100)
    musical = forms.CharField(max_length = 100)

class ArtistForm(forms.Form):
    name = forms.CharField(max_length=100)
    surname = forms.CharField(max_length=100)
    musical = forms.CharField(max_length=100)
    date_of_birth = forms.DateField()

class SearchSongForm(forms.Form):
    criterio_song = forms.CharField(max_length=100)


