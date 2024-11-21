from django.shortcuts import render
from .models import Cliente
from django.contrib import messages

# Create your views here.
def Registro(request):
  if request.method == 'POST':
    nombre = request.POST.get('nombreCliente')
    apellidos = request.POST.get('apellidoCliente')
    correo = request.POST.get('correoCliente')

    nuevoCliente = Cliente(
      NOMBRES = nombre,
      APELLIDOS = apellidos,
      CORREO = correo
    )
    nuevoCliente.save()

    messages.success(
      request, f"Felicitaciones, el cliente {nombre} fue registrado correctamente 😉")
    
    return render(request, 'pages/inicio.html')
    
  return render(request, 'pages/registroCliente.html')