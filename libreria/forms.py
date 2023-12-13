from django import forms
from .models import Libro

class Formulario_Libro(forms.ModelForm):

    class Meta:
        model = Libro
        fields = ("titulo","autores","editorial","fechaPublicacion","genero","isbn","resumen","portada")