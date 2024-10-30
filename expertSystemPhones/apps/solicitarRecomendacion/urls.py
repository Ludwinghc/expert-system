from django.urls import path
from . import views

urlpatterns =[
  path("recomendacion/", views.Recomendacion, name="Recomendacion")
]