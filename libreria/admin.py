from django.contrib import admin
from libreria.models import Usuario, Libro, Editorial, Autor, Prestamo

# Register your models here.
admin.site.register(Usuario)
admin.site.register(Libro)
admin.site.register(Editorial)
admin.site.register(Autor)
admin.site.register(Prestamo)