from django.urls import path
from libreria.views import Libreria, DetalleLibro, NuevoLibro, EditarLibro

urlpatterns = [
    path('', Libreria.as_view(), name="Libreria"),
    path('libro/<int:pk>', DetalleLibro.as_view(), name="Libro"),
    path('nuevo_libro', NuevoLibro.as_view(), name="Nuevo_Libro"),
    path('editar_libro/<int:pk>', EditarLibro.as_view(), name="Editar_Libro"),
    path('eliminar_libro/<int:pk>', EditarLibro.as_view(), name="Eliminar_Libro"),
]
