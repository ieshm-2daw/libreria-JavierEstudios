from django.urls import path, include
from libreria.views import Libreria, DetalleLibro, NuevoLibro, EditarLibro, EliminarLibro, LibreriaDisponibles, LibreriaPrestados, PrestarLibro

urlpatterns = [
    path('', Libreria.as_view(), name="Libreria"),
    path('cuentas', include('django.contrib.auth.urls')),
    path('libro_<int:pk>', DetalleLibro.as_view(), name="Libro"),
    path('nuevo_libro', NuevoLibro.as_view(), name="Nuevo_Libro"),
    path('editar_<int:pk>', EditarLibro.as_view(), name="Editar_Libro"),
    path('eliminar_<int:pk>', EliminarLibro.as_view(), name="Eliminar_Libro"),
    path('disponibles', LibreriaDisponibles.as_view(), name="Disponibles"),
    path('prestar_<int:pk>', PrestarLibro.as_view(), name='Prestar_Libro'),
    path('prestados', LibreriaPrestados.as_view(), name='Prestados'),
]

