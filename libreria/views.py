from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from libreria.models import Libro

from .forms import Formulario_Libro

class Libreria(ListView):
    model = Libro
    template_name = 'libreria.html'

class DetalleLibro(DetailView):
    model = Libro
    template_name = 'libro.html'

class NuevoLibro (CreateView):
    model = Libro
    fields = ["titulo","autores","editorial","fechaPublicacion","genero","isbn","resumen","disponibilidad","portada"]
    template_name = 'nuevo_libro.html'
    success_url = reverse_lazy('Libreria')

class EditarLibro (UpdateView):
    model = Libro
    fields = ["titulo","autores","editorial","fechaPublicacion","genero","isbn","resumen","disponibilidad","portada"]
    template_name = 'editar_libro.html'
    success_url = reverse_lazy('Libreria')

class EditarLibro (DeleteView):
    model = Libro
    template_name = 'eliminar_libro.html'
    success_url = reverse_lazy('Libreria')