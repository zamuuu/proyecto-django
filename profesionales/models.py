from django.db import models

# Create your models here.


class Cerrajero(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=30)
    desempleado = models.BooleanField()


class Futbolista(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=30)
    club_futbol = models.CharField(max_length=50)
    
class VideoJuego(models.Model):
    juego = models.CharField(max_length=30)
    modalidad_juego = models.CharField(max_length=20)
    entretenido = models.BooleanField()