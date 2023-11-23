from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    dni = models.CharField(max_length=9)
    dirección = models.CharField(max_length=100)
    telefono = models.IntegerField()

    def __str__ (self):
        return self.dni

class Libro(models.Model):
    titulo = models.CharField(max_length=100)
    autores = models.CharField(max_length=50)
    editorial = models.CharField(max_length=50)
    fechaPublicacion = models.DateField()
    genero = models.CharField(max_length=100)
    isbn = models.IntegerField()
    resumen = models.TextField()
    disponibilidad = models.CharField(max_length=22)
    portada = models.ImageField(upload_to='libro')

    def __str__ (self):
        return self.isbn

class Autor(models.Model):
    nombre = models.CharField(max_length=50)
    bibliografia = models.TextField()
    foto = models.ImageField(upload_to='autor')

    def __str__ (self):
        return self.nombre

class Editorial(models.Model):
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    sitioWeb = models.CharField(max_length=50)

    def __str__ (self):
        return self.nombre

class Prestamo(models.Model):
    libroPrestado = models.CharField(max_length=100)
    fechaPrestamo = models.DateField()
    fechaDevolucion = models.DateField()
    usuario = models.CharField(max_length=50)
    estado = models.CharField(max_length=50)

    def __str__ (self):
        return self.libroPrestado

