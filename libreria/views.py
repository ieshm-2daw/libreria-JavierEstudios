from datetime import date
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views import View
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
    fields = ["titulo","autores","editorial","fechaPublicacion","genero","isbn","resumen","disponibilidad","portada"]
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
    
class PrestarLibro(View):
    template_name = 'prestamo.html'
    def get(self, request, pk):
        libro = get_object_or_404(Libro, pk = pk)
        return render(request, 'prestamo.html', {'libro':libro})
    
    def post(self, request, pk):
        libro = get_object_or_404(Libro, pk = pk)
        libro.disponibilidad = 'prestado'
        libro.save()

        Prestamo.objects.create(
            libro = libro,
            usuario = request.usuario,
            fechaPrestamo = date.today()
        )
        return redirect('Disponibles', pk = pk)

class LibreriaPrestados(ListView):
    model = Libro
    template_name = 'libreria_prestados.html'

    libros_prestados = Libro.objects.filter(disponibilidad="prestado")