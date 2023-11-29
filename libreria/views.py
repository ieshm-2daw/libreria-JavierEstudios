from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from libreria.models import Libro

from .forms import Formulario_Libro

class Libreria(ListView):
    model = Libro
    template_name = 'libreria.html'

class Libro(DetailView):
    model = Libro

class Nuevo(CreateView):
    model = Libro
    fields = ["titulo","autores","editorial","fechaPublicacion","genero","isbn","resumen","disponibilidad","portada"]
    template_name = 'nuevo_libro.html'
    success_url = reverse_lazy('Liberia')