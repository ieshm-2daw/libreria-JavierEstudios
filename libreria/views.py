from typing import Any
from django.db.models.query import QuerySet
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from libreria.models import Libro, Prestamo

class Libreria(ListView):
    model = Libro
    template_name = 'libreria.html'

class DetalleLibro(DetailView):
    model = Libro
    template_name = 'libro.html'

class NuevoLibro (CreateView):
    model = Libro
    fields = ["titulo","autores","editorial","fechaPublicacion","genero","isbn","resumen","portada"]
    template_name = 'nuevo_libro.html'
    success_url = reverse_lazy('Libreria')

class EditarLibro (UpdateView):
    model = Libro
    fields = ["titulo","autores","editorial","fechaPublicacion","genero","isbn","resumen","portada"]
    template_name = 'editar_libro.html'
    success_url = reverse_lazy('Libreria')

class EliminarLibro (DeleteView):
    model = Libro
    template_name = 'eliminar_libro.html'
    success_url = reverse_lazy('Libreria')

class LibreriaDisponibles(ListView):
    model = Libro
    template_name = 'libreria_disponibles.html'

    def get_queryset(self):
        disponibles = Libro.objects.filter(disponibilidad="disponible")
        return disponibles

class LibreriaPrestados(ListView):
    model = Prestamo
    template_name = 'libreria_prestados.html'
    