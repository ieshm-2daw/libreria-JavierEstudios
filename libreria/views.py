from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from libreria.models import Libro

class Libreria(ListView):
    model = Libro
    template_name = 'libreria.html'

class Libro(DetailView):
    model = Libro

class Nuevo(CreateView):
    model = Libro
    fields = []
    template_name = 'nuevo_libro.html'