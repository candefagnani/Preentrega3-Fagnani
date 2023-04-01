from django.db import models

# Creo el modelo Musical
class Musical(models.Model):
    musical = models.TextField(max_length = 100)
    year_of_opening = models.TextField(max_length = 100)

    def __str__(self):
        return f"Nombre del musical: {self.musical} - Fecha de estreno: {self.year_of_opening}"
    
class Artist(models.Model):
    name = models.TextField(max_length=100)
    surname = models.TextField(max_length=100)
    musical = models.TextField(max_length=100)
    date_of_birth = models.DateField()

    def __str__(self):
        return f"La/El artista {self.name} {self.surname} nació el {self.date_of_birth} y fue parte del musical {self.musical}"
    
class Song(models.Model):
    song = models.TextField(max_length=100)
    duration = models.TextField(max_length=100)
    musical = models.TextField(max_length = 100)

    def __str__(self):
        return f"La canción {self.song} pertenece al musical {self.musical} y tiene un tiempo de duración de {self.duration} minutos"
