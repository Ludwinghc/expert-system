from django.shortcuts import render
from apps.registrarClientes.models import Pregunta, Respuesta

# Create your views here.
def Recomendacion(request):
  # Crear una lista para almacenar cada pregunta y sus respuestas
  preguntas_con_respuestas = []

  # Obtener todas las preguntas y las respuestas relacionadas
  preguntas = Pregunta.objects.all()
  for pregunta in preguntas:
      # Filtrar respuestas que pertenecen a la pregunta actual
      respuestas = Respuesta.objects.filter(ID_PREGUNTAS=pregunta.ID_PREGUNTAS).values('ID_PREGUNTAS', 'RESPUESTA')
      # Agregar la pregunta con sus respuestas a la lista
      preguntas_con_respuestas.append({
          'pregunta': pregunta,
          'respuestas': respuestas
      })
  
  contexto = {
      'preguntas_con_respuestas': preguntas_con_respuestas
  }
  return render(request, 'pages/recomendacion.html', contexto)