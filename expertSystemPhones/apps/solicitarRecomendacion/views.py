from django.shortcuts import render
from django.db import connection
from apps.registrarClientes.models import Pregunta, Respuesta, Cliente
from apps.solicitarRecomendacion.models import Recomendacion
from django.core.mail import EmailMessage 
from django.conf import settings
from django.contrib import messages  # Para usar mensajes flash
from django.template.loader import render_to_string
from apps.solicitarRecomendacion.utils.recomendation import recomendation_phone

# Create your views here.
def Recomendacion(request):
	if request.method == 'POST':
		pregunta1 = request.POST.get('pregunta_1')
		pregunta2 = request.POST.get('pregunta_2')
		pregunta3 = request.POST.get('pregunta_3')
		pregunta4 = request.POST.get('pregunta_4')
		pregunta5 = request.POST.get('pregunta_5')
		pregunta6 = request.POST.get('pregunta_6')
		
		# Obtener el ultimo ID del cliente registrado
		ultimo_cliente = Cliente.objects.last()
		if ultimo_cliente:
			ultimo_id = ultimo_cliente.ID_CLIENTE

		print(f'el ultimo id es: {ultimo_id}')
		recomendacion = recomendation_phone(
		pregunta1=pregunta1,
		pregunta2=pregunta2,
		pregunta3=pregunta3,
		pregunta4=pregunta4,
		pregunta5=pregunta5,
		pregunta6=pregunta6)	

		celulares = []
					# ENVIAR LA RECOMENDACION AL CORREO DEL ULTIMO CLIENTE REGISTRADO
		correo_response = Cliente.objects.last().CORREO
		correo_cliente = correo_response

		# lOGICA PARA REGISTRAR LA RECOMENDACION
		if not recomendacion:
			recomendacion_response = 'No tengo un celular que se cumpla tus necesidades'
			template_fail = render_to_string('pages/email_fail.html',{
				'mensaje': recomendacion_response
			})
			email = EmailMessage(
				subject = 'Recomendación de celulares',
				body = template_fail,
				from_email = settings.EMAIL_HOST_USER,
				to = [correo_cliente]
			)
			email.fail_silently = False
			email.send()
		else:
			for opcion in recomendacion:
				print(f"Id de la opcion: {opcion['ID_OPCIONES']}")
				print(f"Id de la opcion: {opcion['NOMBRE']}")
				celulares.append(opcion['NOMBRE'])
				with connection.cursor() as cursor:
					cursor.callproc('agregar_recomendacion', [ultimo_id, opcion['ID_OPCIONES']])
			

			
			template = render_to_string('pages/email.html',{
				'Celulares': celulares
			})

			email = EmailMessage(
				subject = 'Recomendación de celulares',
				body = template,
				from_email = settings.EMAIL_HOST_USER,
				to = [correo_cliente]
			)
			email.fail_silently = False
			email.send()

			messages.success(request, f"Tu Recomendación fue enviada a tu correo 😉")


		
		# if recomendacion:
		# 	for opcion in recomendacion:
		# 		id_opcion = opcion['ID_OPCIONES']
		# 		nombre = opcion['NOMBRE']
		# 	with connection.cursor() as cursor:
		# 		cursor.callproc('agregar_recomendacion', [ultimo_id, id_opcion])
		
		return render(request, 'pages/inicio.html')
  # Crear una lista para almacenar cada pregunta y sus respuestas
	preguntas_con_respuestas = []
  # Obtener todas las preguntas y las respuestas relacionadas
	preguntas = Pregunta.objects.all()
	for pregunta in preguntas:
			# Filtrar respuestas que pertenecen a la pregunta actual
			respuestas = Respuesta.objects.filter(ID_PREGUNTAS=pregunta.ID_PREGUNTAS).values('ID_PREGUNTAS', 'RESPUESTA')
			# Agregar la pregunta con sus respuestas a la lista
			preguntas_con_respuestas.append({
					'id': pregunta.ID_PREGUNTAS,
					'pregunta': pregunta.PREGUNTA,
					'respuestas': respuestas
			})
	contexto = {
      'preguntas_con_respuestas': preguntas_con_respuestas
			}
	return render(request, 'pages/recomendacion.html', contexto)

def Filtro(request):
	return render(request, 'pages/filtro.html')