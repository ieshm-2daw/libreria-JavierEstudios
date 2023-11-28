from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    dni = models.CharField(max_length=9)
    dirección = models.CharField(max_length=100)
    telefono = models.IntegerField()

    def __str__ (self):
        return self.dni

class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    bibliografia = models.TextField()
    foto = models.ImageField(upload_to='autores/', null=True, blank=True)

    def __str__ (self):
        return self.nombre

class Editorial(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    sitioWeb = models.URLField()

    def __str__ (self):
        return self.nombre
    
class Libro(models.Model):
    CHOICES_DISPONIBILIDAD = [
        ('disponible', 'Disponible'),
        ('prestado', 'Prestado'),
        ('en_proceso', 'En proceso de prestamo'),
    ]
    titulo = models.CharField(max_length=100)
    autores = models.ManyToManyField(Autor)
    editorial = models.ForeignKey(Editorial, on_delete=models.CASCADE)
    fechaPublicacion = models.DateField()
    genero = models.CharField(max_length=100)
    isbn = models.CharField(max_length=13)
    resumen = models.TextField()
    disponibilidad = models.CharField(max_length=10 , choices=CHOICES_DISPONIBILIDAD)
    portada = models.ImageField(upload_to='libros/', null=True, blank=True)

    def __str__ (self):
        return self.titulo

class Prestamo(models.Model):
    libroPrestado = models.ManyToManyField(Libro)
    fechaPrestamo = models.DateField()
    fechaDevolucion = models.DateField(null=True, blank=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    estado = models.CharField(max_length=50)

    def __str__ (self):
        return f"{self.libroPrestado.titulo} {self.fechaPrestamo}"
