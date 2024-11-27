from django.urls import path
from . import views

urlpatterns =[
  path("registrarCliente/", views.Registro, name="Registro")
]