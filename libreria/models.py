from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    dni = models.CharField(max_length=9)
    dirección = models.CharField(max_length=100)
    telefono = models.IntegerField(max_length=9)

class Libro(models.Model):
    titulo = models.CharField(max_length=100)
    autores = models.ManyToManyRel()
    editorial = models.ManyToOneRel()
    fechaPublicacion = models.DateField()
    genero = models.CharField(max_length=100)

    portada = models.ImageField()
