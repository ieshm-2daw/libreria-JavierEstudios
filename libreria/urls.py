from django.urls import path
from .views import Libreria, Libro, Nuevo 

urlpatterns = [
    path('', Libreria.as_view(), name="Libreria"),
    path('libro/<int:pk>', Libro.as_view(), name="Libro"),
    path('nuevo_libro', Nuevo.as_view(), name="Nuevo_Libro"),
]
