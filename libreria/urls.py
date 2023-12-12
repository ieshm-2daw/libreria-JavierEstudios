from django.urls import path
from libreria.views import Libreria, DetalleLibro, NuevoLibro

urlpatterns = [
    path('', Libreria.as_view(), name="Libreria"),
    path('libro/<int:pk>', DetalleLibro.as_view(), name="Libro"),
    path('nuevo_libro', NuevoLibro.as_view(), name="Nuevo_Libro"),
]
