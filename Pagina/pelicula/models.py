from django.db import models

# Create your models here.


class Pelicula(models.Model):
    titulo = models.CharField(max_length=50, unique=True)
    director = models.CharField(max_length=50)
    creado = models.DateTimeField(auto_now=True)

class Elenco(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)

class Musica(models.Model):
    cancion = models.CharField(max_length=50, unique=True)
    interprete = models.CharField(max_length=50)