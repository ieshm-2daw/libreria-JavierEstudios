from django.urls import path
from .views import Libreria 

urlpatterns = [
    path('', Libreria.as_view(), name="Libreria"),
]
