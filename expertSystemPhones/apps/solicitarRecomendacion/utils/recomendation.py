from apps.solicitarRecomendacion.models import Opciones
def recomendation_phone(pregunta1, pregunta2, pregunta3, pregunta4, pregunta5, pregunta6):
  #! RECOMENDACIONES PARA USO BASICO Y PRODUCTIVIDAD
  #! PRESUPUESTO 1
  #? SAMSUNG Galaxy A05 
  if pregunta1 == 'Uso basico y productividad' and pregunta2 == '100.000$ - 500.000$' and pregunta3 == '64 GigaBytes' and pregunta4 == '4 GygaBytes' and pregunta5 == '50 Megapixeles' and pregunta6 == '5000 Mph':
    opciones = Opciones.objects.filter(PROPOSITO = pregunta1, PRESUPUESTO = pregunta2, ALMACENAMIENTO = pregunta3, RAM = pregunta4, CAMARA = pregunta5, BATERIA = pregunta6).values('ID_OPCIONES','NOMBRE')
    return list(opciones)
  # ? XIAOMI REDMI 13C
  elif pregunta1 == 'Uso basico y productividad' and pregunta2 == '100.000$ - 500.000$' and pregunta3 == '128 GigaBytes' and pregunta4 == '4 GygaBytes' and pregunta5 == '50 Megapixeles' and pregunta6 == '5000 Mph':
    opciones = Opciones.objects.filter(PROPOSITO = pregunta1, PRESUPUESTO = pregunta2, ALMACENAMIENTO = pregunta3, RAM = pregunta4, CAMARA = pregunta5, BATERIA = pregunta6).values('ID_OPCIONES','NOMBRE')
    return list(opciones)
  #? KALLEY BLACK Z
  elif pregunta1 == 'Uso basico y productividad' and pregunta2 == '100.000$ - 500.000$' and pregunta3 == '256 GigaBytes' and pregunta4 == '6 GygaBytes' and pregunta5 == '50 Megapixeles' and pregunta6 == '5000 Mph':
    opciones = Opciones.objects.filter(PROPOSITO = pregunta1, PRESUPUESTO = pregunta2, ALMACENAMIENTO = pregunta3, RAM = pregunta4, CAMARA = pregunta5, BATERIA = pregunta6).values('ID_OPCIONES','NOMBRE')
    return list(opciones)
  

  #! PRESUPUESTO 2
  # ? Celular TCL 50Pro
  elif pregunta1 == 'Uso basico y productividad' and pregunta2 == '500.000$ - 1.000.000$' and pregunta3 == '512 GigaBytes' and pregunta4 == '8 GygaBytes' and pregunta5 == '108 Megapixeles' and pregunta6 == '5200 Mph':
    opciones = Opciones.objects.filter(PROPOSITO = pregunta1, PRESUPUESTO = pregunta2, ALMACENAMIENTO = pregunta3, RAM = pregunta4, CAMARA = pregunta5, BATERIA = pregunta6).values('ID_OPCIONES','NOMBRE')
    return list(opciones)
  # ?  HUAWEI Nova 10 SE
  elif pregunta1 == 'Uso basico y productividad' and pregunta2 == '500.000$ - 1.000.000$' and pregunta3 == '128 GigaBytes' and pregunta4 == '8 GygaBytes' and pregunta5 == '108 Megapixeles' and pregunta6 == '4500 Mph':
    opciones = Opciones.objects.filter(PROPOSITO = pregunta1, PRESUPUESTO = pregunta2, ALMACENAMIENTO = pregunta3, RAM = pregunta4, CAMARA = pregunta5, BATERIA = pregunta6).values('ID_OPCIONES','NOMBRE')
    return list(opciones)
  # ? VIVO Y03 
  elif pregunta1 == 'Uso basico y productividad' and pregunta2 == '500.000$ - 1.000.000$' and pregunta3 == '128 GigaBytes' and pregunta4 == '4 GygaBytes' and pregunta5 == '13 Megapixeles' and pregunta6 == '5000 Mph':
    opciones = Opciones.objects.filter(PROPOSITO = pregunta1, PRESUPUESTO = pregunta2, ALMACENAMIENTO = pregunta3, RAM = pregunta4, CAMARA = pregunta5, BATERIA = pregunta6).values('ID_OPCIONES','NOMBRE')
    return list(opciones)
  

  #! PRESUPUESTO 3
  # ? iPhone 11
  elif pregunta1 == 'Uso basico y productividad' and pregunta2 == '1.000.000$ - 2.000.000$' and pregunta3 == '64 GigaBytes' and pregunta4 == '4 GygaBytes' and pregunta5 == '12 Megapixeles' and pregunta6 == '3110 Mph':
    opciones = Opciones.objects.filter(PROPOSITO = pregunta1, PRESUPUESTO = pregunta2, ALMACENAMIENTO = pregunta3, RAM = pregunta4, CAMARA = pregunta5, BATERIA = pregunta6).values('ID_OPCIONES','NOMBRE')
    return list(opciones)
  # ? VIVO V25
  elif pregunta1 == 'Uso basico y productividad' and pregunta2 == '1.000.000$ - 2.000.000$' and pregunta3 == '128 GigaBytes' and pregunta4 == '8 GygaBytes' and pregunta5 == '64 Megapixeles' and pregunta6 == '4500 Mph':
    opciones = Opciones.objects.filter(PROPOSITO = pregunta1, PRESUPUESTO = pregunta2, ALMACENAMIENTO = pregunta3, RAM = pregunta4, CAMARA = pregunta5, BATERIA = pregunta6).values('ID_OPCIONES','NOMBRE')
    return list(opciones)
  # ? MOTOROLA Edge50 Neo
  elif pregunta1 == 'Uso basico y productividad' and pregunta2 == '1.000.000$ - 2.000.000$' and pregunta3 == '256 GigaBytes' and pregunta4 == '8 GygaBytes' and pregunta5 == '50 Megapixeles' and pregunta6 == '4400 Mph':
    opciones = Opciones.objects.filter(PROPOSITO = pregunta1, PRESUPUESTO = pregunta2, ALMACENAMIENTO = pregunta3, RAM = pregunta4, CAMARA = pregunta5, BATERIA = pregunta6).values('ID_OPCIONES','NOMBRE')
    return list(opciones)
  


  #! PRESUPUESTO 4
  # ? iPhone 13 
  elif pregunta1 == 'Uso basico y productividad' and pregunta2 == '2.000.000$ - 3.000.000$' and pregunta3 == '128 GigaBytes' and pregunta4 == '6 GygaBytes' and pregunta5 == '12 Megapixeles' and pregunta6 == '3110 Mph':
    opciones = Opciones.objects.filter(PROPOSITO = pregunta1, PRESUPUESTO = pregunta2, ALMACENAMIENTO = pregunta3, RAM = pregunta4, CAMARA = pregunta5, BATERIA = pregunta6).values('ID_OPCIONES','NOMBRE')
    return list(opciones)
  # ? HONOR H200
  elif pregunta1 == 'Uso basico y productividad' and pregunta2 == '2.000.000$ - 3.000.000$' and pregunta3 == '256 GigaBytes' and pregunta4 == '12 GygaBytes' and pregunta5 == '50 Megapixeles' and pregunta6 == '5200 Mph':
    opciones = Opciones.objects.filter(PROPOSITO = pregunta1, PRESUPUESTO = pregunta2, ALMACENAMIENTO = pregunta3, RAM = pregunta4, CAMARA = pregunta5, BATERIA = pregunta6).values('ID_OPCIONES','NOMBRE')
    return list(opciones)
  # ? Xiaomi 14T
  elif pregunta1 == 'Uso basico y productividad' and pregunta2 == '2.000.000$ - 3.000.000$' and pregunta3 == '512 GigaBytes' and pregunta4 == '12 GygaBytes' and pregunta5 == '50 Megapixeles' and pregunta6 == '5000 Mph':
    opciones = Opciones.objects.filter(PROPOSITO = pregunta1, PRESUPUESTO = pregunta2, ALMACENAMIENTO = pregunta3, RAM = pregunta4, CAMARA = pregunta5, BATERIA = pregunta6).values('ID_OPCIONES','NOMBRE')
    return list(opciones)
  


  #! PRESUPUESTO 5
  # ? iPhone 12
  elif pregunta1 == 'Uso basico y productividad' and pregunta2 == '3.000.000$ - 5.000.000$' and pregunta3 == '64 GigaBytes' and pregunta4 == '4 GygaBytes' and pregunta5 == '12 Megapixeles' and pregunta6 == '3110 Mph':
    opciones = Opciones.objects.filter(PROPOSITO = pregunta1, PRESUPUESTO = pregunta2, ALMACENAMIENTO = pregunta3, RAM = pregunta4, CAMARA = pregunta5, BATERIA = pregunta6).values('ID_OPCIONES','NOMBRE')
    return list(opciones)
  # ? iPhone 15
  elif pregunta1 == 'Uso basico y productividad' and pregunta2 == '3.000.000$ - 5.000.000$' and pregunta3 == '128 GigaBytes' and pregunta4 == '6 GygaBytes' and pregunta5 == '12 Megapixeles' and pregunta6 == '3877 Mph':
    opciones = Opciones.objects.filter(PROPOSITO = pregunta1, PRESUPUESTO = pregunta2, ALMACENAMIENTO = pregunta3, RAM = pregunta4, CAMARA = pregunta5, BATERIA = pregunta6).values('ID_OPCIONES','NOMBRE')
    return list(opciones)
  # ? HUAWEI P60 Pro
  elif pregunta1 == 'Uso basico y productividad' and pregunta2 == '3.000.000$ - 5.000.000$' and pregunta3 == '256 GigaBytes' and pregunta4 == '8 GygaBytes' and pregunta5 == '48 Megapixeles' and pregunta6 == '5800 Mph':
    opciones = Opciones.objects.filter(PROPOSITO = pregunta1, PRESUPUESTO = pregunta2, ALMACENAMIENTO = pregunta3, RAM = pregunta4, CAMARA = pregunta5, BATERIA = pregunta6).values('ID_OPCIONES','NOMBRE')
    return list(opciones)
  # ? SAMSUNG Galaxy S24FE
  elif pregunta1 == 'Uso basico y productividad' and pregunta2 == '3.000.000$ - 5.000.000$' and pregunta3 == '512 GigaBytes' and pregunta4 == '8 GygaBytes' and pregunta5 == '50 Megapixeles' and pregunta6 == '4500 Mph':
    opciones = Opciones.objects.filter(PROPOSITO = pregunta1, PRESUPUESTO = pregunta2, ALMACENAMIENTO = pregunta3, RAM = pregunta4, CAMARA = pregunta5, BATERIA = pregunta6).values('ID_OPCIONES','NOMBRE')
    return list(opciones)
  


  #! PRESUPUESTO 6
  # ? iPhone 16 Pro
  elif pregunta1 == 'Uso basico y productividad' and pregunta2 == '5.000.000$ - MAS' and pregunta3 == '128 GigaBytes' and pregunta4 == '8 GygaBytes' and pregunta5 == '48 Megapixeles' and pregunta6 == '3900 Mph':
    opciones = Opciones.objects.filter(PROPOSITO = pregunta1, PRESUPUESTO = pregunta2, ALMACENAMIENTO = pregunta3, RAM = pregunta4, CAMARA = pregunta5, BATERIA = pregunta6).values('ID_OPCIONES','NOMBRE')
    return list(opciones)
  # ? Galaxy Z Flip6
  elif pregunta1 == 'Uso basico y productividad' and pregunta2 == '5.000.000$ - MAS' and pregunta3 == '256 GigaBytes' and pregunta4 == '12 GygaBytes' and pregunta5 == '50 Megapixeles' and pregunta6 == '4000 Mph':
    opciones = Opciones.objects.filter(PROPOSITO = pregunta1, PRESUPUESTO = pregunta2, ALMACENAMIENTO = pregunta3, RAM = pregunta4, CAMARA = pregunta5, BATERIA = pregunta6).values('ID_OPCIONES','NOMBRE')
    return list(opciones)
  # ? Galaxy Z Fold6
  elif pregunta1 == 'Uso basico y productividad' and pregunta2 == '5.000.000$ - MAS' and pregunta3 == '512 GigaBytes' and pregunta4 == '4 GygaBytes' and pregunta5 == '50 Megapixeles' and pregunta6 == '4500 Mph':
    opciones = Opciones.objects.filter(PROPOSITO = pregunta1, PRESUPUESTO = pregunta2, ALMACENAMIENTO = pregunta3, RAM = pregunta4, CAMARA = pregunta5, BATERIA = pregunta6).values('ID_OPCIONES','NOMBRE')
    return list(opciones)
  # ? HUAWEI Pura70 Ultra
  elif pregunta1 == 'Uso basico y productividad' and pregunta2 == '5.000.000$ - MAS' and pregunta3 == '512 GigaBytes' and pregunta4 == '16 GygaBytes' and pregunta5 == '50 Megapixeles' and pregunta6 == '5200 Mph':
    opciones = Opciones.objects.filter(PROPOSITO = pregunta1, PRESUPUESTO = pregunta2, ALMACENAMIENTO = pregunta3, RAM = pregunta4, CAMARA = pregunta5, BATERIA = pregunta6).values('ID_OPCIONES','NOMBRE')
    return list(opciones)
  


  #! RECOMENDACIONES PARA Creador de contenido
  #? SAMSUNG Galaxy A05 
  if pregunta1 == 'Creador de contenido' and pregunta2 == '100.000$ - 500.000$' and pregunta3 == '64 GigaBytes' and pregunta4 == '4 GygaBytes' and pregunta5 == '50 Megapixeles' and pregunta6 == '5000 Mph':
    opciones = Opciones.objects.filter(PROPOSITO = pregunta1, PRESUPUESTO = pregunta2, ALMACENAMIENTO = pregunta3, RAM = pregunta4, CAMARA = pregunta5, BATERIA = pregunta6).values('ID_OPCIONES','NOMBRE')
    return list(opciones)
  # ? XIAOMI REDMI 13C
  elif pregunta1 == 'Creador de contenido' and pregunta2 == '100.000$ - 500.000$' and pregunta3 == '128 GigaBytes' and pregunta4 == '4 GygaBytes' and pregunta5 == '50 Megapixeles' and pregunta6 == '5000 Mph':
    opciones = Opciones.objects.filter(PROPOSITO = pregunta1, PRESUPUESTO = pregunta2, ALMACENAMIENTO = pregunta3, RAM = pregunta4, CAMARA = pregunta5, BATERIA = pregunta6).values('ID_OPCIONES','NOMBRE')
    return list(opciones)
  #? KALLEY BLACK Z
  elif pregunta1 == 'Creador de contenido' and pregunta2 == '100.000$ - 500.000$' and pregunta3 == '256 GigaBytes' and pregunta4 == '6 GygaBytes' and pregunta5 == '50 Megapixeles' and pregunta6 == '5000 Mph':
    opciones = Opciones.objects.filter(PROPOSITO = pregunta1, PRESUPUESTO = pregunta2, ALMACENAMIENTO = pregunta3, RAM = pregunta4, CAMARA = pregunta5, BATERIA = pregunta6).values('ID_OPCIONES','NOMBRE')
    return list(opciones)
  # ? Celular TCL 50Pro
  elif pregunta1 == 'Creador de contenido' and pregunta2 == '500.000$ - 1.000.000$' and pregunta3 == '512 GigaBytes' and pregunta4 == '8 GygaBytes' and pregunta5 == '108 Megapixeles' and pregunta6 == '5200 Mph':
    opciones = Opciones.objects.filter(PROPOSITO = pregunta1, PRESUPUESTO = pregunta2, ALMACENAMIENTO = pregunta3, RAM = pregunta4, CAMARA = pregunta5, BATERIA = pregunta6).values('ID_OPCIONES','NOMBRE')
    return list(opciones)
  # ?  HUAWEI Nova 10 SE
  elif pregunta1 == 'Creador de contenido' and pregunta2 == '500.000$ - 1.000.000$' and pregunta3 == '128 GigaBytes' and pregunta4 == '8 GygaBytes' and pregunta5 == '108 Megapixeles' and pregunta6 == '4500 Mph':
    opciones = Opciones.objects.filter(PROPOSITO = pregunta1, PRESUPUESTO = pregunta2, ALMACENAMIENTO = pregunta3, RAM = pregunta4, CAMARA = pregunta5, BATERIA = pregunta6).values('ID_OPCIONES','NOMBRE')
    return list(opciones)
  # ? VIVO Y03 
  elif pregunta1 == 'Creador de contenido' and pregunta2 == '500.000$ - 1.000.000$' and pregunta3 == '128 GigaBytes' and pregunta4 == '4 GygaBytes' and pregunta5 == '13 Megapixeles' and pregunta6 == '5000 Mph':
    opciones = Opciones.objects.filter(PROPOSITO = pregunta1, PRESUPUESTO = pregunta2, ALMACENAMIENTO = pregunta3, RAM = pregunta4, CAMARA = pregunta5, BATERIA = pregunta6).values('ID_OPCIONES','NOMBRE')
    return list(opciones)
  # ? iPhone 11
  elif pregunta1 == 'Creador de contenido' and pregunta2 == '1.000.000$ - 2.000.000$' and pregunta3 == '64 GigaBytes' and pregunta4 == '4 GygaBytes' and pregunta5 == '12 Megapixeles' and pregunta6 == '3110 Mph':
    opciones = Opciones.objects.filter(PROPOSITO = pregunta1, PRESUPUESTO = pregunta2, ALMACENAMIENTO = pregunta3, RAM = pregunta4, CAMARA = pregunta5, BATERIA = pregunta6).values('ID_OPCIONES','NOMBRE')
    return list(opciones)
  # ? VIVO V25
  elif pregunta1 == 'Creador de contenido' and pregunta2 == '1.000.000$ - 2.000.000$' and pregunta3 == '128 GigaBytes' and pregunta4 == '8 GygaBytes' and pregunta5 == '64 Megapixeles' and pregunta6 == '4500 Mph':
    opciones = Opciones.objects.filter(PROPOSITO = pregunta1, PRESUPUESTO = pregunta2, ALMACENAMIENTO = pregunta3, RAM = pregunta4, CAMARA = pregunta5, BATERIA = pregunta6).values('ID_OPCIONES','NOMBRE')
    return list(opciones)
  # ? MOTOROLA Edge50 Neo
  elif pregunta1 == 'Creador de contenido' and pregunta2 == '1.000.000$ - 2.000.000$' and pregunta3 == '256 GigaBytes' and pregunta4 == '8 GygaBytes' and pregunta5 == '50 Megapixeles' and pregunta6 == '4400 Mph':
    opciones = Opciones.objects.filter(PROPOSITO = pregunta1, PRESUPUESTO = pregunta2, ALMACENAMIENTO = pregunta3, RAM = pregunta4, CAMARA = pregunta5, BATERIA = pregunta6).values('ID_OPCIONES','NOMBRE')
    return list(opciones)
  # ? iPhone 13 
  elif pregunta1 == 'Creador de contenido' and pregunta2 == '2.000.000$ - 3.000.000$' and pregunta3 == '128 GigaBytes' and pregunta4 == '6 GygaBytes' and pregunta5 == '12 Megapixeles' and pregunta6 == '3110 Mph':
    opciones = Opciones.objects.filter(PROPOSITO = pregunta1, PRESUPUESTO = pregunta2, ALMACENAMIENTO = pregunta3, RAM = pregunta4, CAMARA = pregunta5, BATERIA = pregunta6).values('ID_OPCIONES','NOMBRE')
    return list(opciones)
  # ? HONOR H200
  elif pregunta1 == 'Creador de contenido' and pregunta2 == '2.000.000$ - 3.000.000$' and pregunta3 == '256 GigaBytes' and pregunta4 == '12 GygaBytes' and pregunta5 == '50 Megapixeles' and pregunta6 == '5200 Mph':
    opciones = Opciones.objects.filter(PROPOSITO = pregunta1, PRESUPUESTO = pregunta2, ALMACENAMIENTO = pregunta3, RAM = pregunta4, CAMARA = pregunta5, BATERIA = pregunta6).values('ID_OPCIONES','NOMBRE')
    return list(opciones)
  # ? Xiaomi 14T
  elif pregunta1 == 'Creador de contenido' and pregunta2 == '2.000.000$ - 3.000.000$' and pregunta3 == '512 GigaBytes' and pregunta4 == '12 GygaBytes' and pregunta5 == '50 Megapixeles' and pregunta6 == '5000 Mph':
    opciones = Opciones.objects.filter(PROPOSITO = pregunta1, PRESUPUESTO = pregunta2, ALMACENAMIENTO = pregunta3, RAM = pregunta4, CAMARA = pregunta5, BATERIA = pregunta6).values('ID_OPCIONES','NOMBRE')
    return list(opciones)
  # ? iPhone 12
  elif pregunta1 == 'Creador de contenido' and pregunta2 == '3.000.000$ - 5.000.000$' and pregunta3 == '64 GigaBytes' and pregunta4 == '4 GygaBytes' and pregunta5 == '12 Megapixeles' and pregunta6 == '3110 Mph':
    opciones = Opciones.objects.filter(PROPOSITO = pregunta1, PRESUPUESTO = pregunta2, ALMACENAMIENTO = pregunta3, RAM = pregunta4, CAMARA = pregunta5, BATERIA = pregunta6).values('ID_OPCIONES','NOMBRE')
    return list(opciones)
  # ? iPhone 15
  elif pregunta1 == 'Creador de contenido' and pregunta2 == '3.000.000$ - 5.000.000$' and pregunta3 == '128 GigaBytes' and pregunta4 == '6 GygaBytes' and pregunta5 == '12 Megapixeles' and pregunta6 == '3877 Mph':
    opciones = Opciones.objects.filter(PROPOSITO = pregunta1, PRESUPUESTO = pregunta2, ALMACENAMIENTO = pregunta3, RAM = pregunta4, CAMARA = pregunta5, BATERIA = pregunta6).values('ID_OPCIONES','NOMBRE')
    return list(opciones)
  # ? HUAWEI P60 Pro
  elif pregunta1 == 'Creador de contenido' and pregunta2 == '3.000.000$ - 5.000.000$' and pregunta3 == '256 GigaBytes' and pregunta4 == '8 GygaBytes' and pregunta5 == '48 Megapixeles' and pregunta6 == '5800 Mph':
    opciones = Opciones.objects.filter(PROPOSITO = pregunta1, PRESUPUESTO = pregunta2, ALMACENAMIENTO = pregunta3, RAM = pregunta4, CAMARA = pregunta5, BATERIA = pregunta6).values('ID_OPCIONES','NOMBRE')
    return list(opciones)
  # ? SAMSUNG Galaxy S24FE
  elif pregunta1 == 'Creador de contenido' and pregunta2 == '3.000.000$ - 5.000.000$' and pregunta3 == '512 GigaBytes' and pregunta4 == '8 GygaBytes' and pregunta5 == '50 Megapixeles' and pregunta6 == '4500 Mph':
    opciones = Opciones.objects.filter(PROPOSITO = pregunta1, PRESUPUESTO = pregunta2, ALMACENAMIENTO = pregunta3, RAM = pregunta4, CAMARA = pregunta5, BATERIA = pregunta6).values('ID_OPCIONES','NOMBRE')
    return list(opciones)
  # ? iPhone 16 Pro
  elif pregunta1 == 'Creador de contenido' and pregunta2 == '5.000.000$ - MAS' and pregunta3 == '128 GigaBytes' and pregunta4 == '8 GygaBytes' and pregunta5 == '48 Megapixeles' and pregunta6 == '3900 Mph':
    opciones = Opciones.objects.filter(PROPOSITO = pregunta1, PRESUPUESTO = pregunta2, ALMACENAMIENTO = pregunta3, RAM = pregunta4, CAMARA = pregunta5, BATERIA = pregunta6).values('ID_OPCIONES','NOMBRE')
    return list(opciones)
  # ? Galaxy Z Flip6
  elif pregunta1 == 'Creador de contenido' and pregunta2 == '5.000.000$ - MAS' and pregunta3 == '256 GigaBytes' and pregunta4 == '12 GygaBytes' and pregunta5 == '50 Megapixeles' and pregunta6 == '4000 Mph':
    opciones = Opciones.objects.filter(PROPOSITO = pregunta1, PRESUPUESTO = pregunta2, ALMACENAMIENTO = pregunta3, RAM = pregunta4, CAMARA = pregunta5, BATERIA = pregunta6).values('ID_OPCIONES','NOMBRE')
    return list(opciones)
  # ? Galaxy Z Fold6
  elif pregunta1 == 'Creador de contenido' and pregunta2 == '5.000.000$ - MAS' and pregunta3 == '512 GigaBytes' and pregunta4 == '4 GygaBytes' and pregunta5 == '50 Megapixeles' and pregunta6 == '4500 Mph':
    opciones = Opciones.objects.filter(PROPOSITO = pregunta1, PRESUPUESTO = pregunta2, ALMACENAMIENTO = pregunta3, RAM = pregunta4, CAMARA = pregunta5, BATERIA = pregunta6).values('ID_OPCIONES','NOMBRE')
    return list(opciones)
  # ? HUAWEI Pura70 Ultra
  elif pregunta1 == 'Creador de contenido' and pregunta2 == '5.000.000$ - MAS' and pregunta3 == '512 GigaBytes' and pregunta4 == '16 GygaBytes' and pregunta5 == '50 Megapixeles' and pregunta6 == '5200 Mph':
    opciones = Opciones.objects.filter(PROPOSITO = pregunta1, PRESUPUESTO = pregunta2, ALMACENAMIENTO = pregunta3, RAM = pregunta4, CAMARA = pregunta5, BATERIA = pregunta6).values('ID_OPCIONES','NOMBRE')
    return list(opciones)
  #! RECOMENDACIONES PARA Gamming y entretenimiento
  #? SAMSUNG Galaxy A05 
  if pregunta1 == 'Gamming y entretenimiento' and pregunta2 == '100.000$ - 500.000$' and pregunta3 == '64 GigaBytes' and pregunta4 == '4 GygaBytes' and pregunta5 == '50 Megapixeles' and pregunta6 == '5000 Mph':
    opciones = Opciones.objects.filter(PROPOSITO = pregunta1, PRESUPUESTO = pregunta2, ALMACENAMIENTO = pregunta3, RAM = pregunta4, CAMARA = pregunta5, BATERIA = pregunta6).values('ID_OPCIONES','NOMBRE')
    return list(opciones)
  # ? XIAOMI REDMI 13C
  elif pregunta1 == 'Gamming y entretenimiento' and pregunta2 == '100.000$ - 500.000$' and pregunta3 == '128 GigaBytes' and pregunta4 == '4 GygaBytes' and pregunta5 == '50 Megapixeles' and pregunta6 == '5000 Mph':
    opciones = Opciones.objects.filter(PROPOSITO = pregunta1, PRESUPUESTO = pregunta2, ALMACENAMIENTO = pregunta3, RAM = pregunta4, CAMARA = pregunta5, BATERIA = pregunta6).values('ID_OPCIONES','NOMBRE')
    return list(opciones)
  #? KALLEY BLACK Z
  elif pregunta1 == 'Gamming y entretenimiento' and pregunta2 == '100.000$ - 500.000$' and pregunta3 == '256 GigaBytes' and pregunta4 == '6 GygaBytes' and pregunta5 == '50 Megapixeles' and pregunta6 == '5000 Mph':
    opciones = Opciones.objects.filter(PROPOSITO = pregunta1, PRESUPUESTO = pregunta2, ALMACENAMIENTO = pregunta3, RAM = pregunta4, CAMARA = pregunta5, BATERIA = pregunta6).values('ID_OPCIONES','NOMBRE')
    return list(opciones)
  # ? Celular TCL 50Pro
  elif pregunta1 == 'Gamming y entretenimiento' and pregunta2 == '500.000$ - 1.000.000$' and pregunta3 == '512 GigaBytes' and pregunta4 == '8 GygaBytes' and pregunta5 == '108 Megapixeles' and pregunta6 == '5200 Mph':
    opciones = Opciones.objects.filter(PROPOSITO = pregunta1, PRESUPUESTO = pregunta2, ALMACENAMIENTO = pregunta3, RAM = pregunta4, CAMARA = pregunta5, BATERIA = pregunta6).values('ID_OPCIONES','NOMBRE')
    return list(opciones)
  # ?  HUAWEI Nova 10 SE
  elif pregunta1 == 'Gamming y entretenimiento' and pregunta2 == '500.000$ - 1.000.000$' and pregunta3 == '128 GigaBytes' and pregunta4 == '8 GygaBytes' and pregunta5 == '108 Megapixeles' and pregunta6 == '4500 Mph':
    opciones = Opciones.objects.filter(PROPOSITO = pregunta1, PRESUPUESTO = pregunta2, ALMACENAMIENTO = pregunta3, RAM = pregunta4, CAMARA = pregunta5, BATERIA = pregunta6).values('ID_OPCIONES','NOMBRE')
    return list(opciones)
  # ? VIVO Y03 
  elif pregunta1 == 'Gamming y entretenimiento' and pregunta2 == '500.000$ - 1.000.000$' and pregunta3 == '128 GigaBytes' and pregunta4 == '4 GygaBytes' and pregunta5 == '13 Megapixeles' and pregunta6 == '5000 Mph':
    opciones = Opciones.objects.filter(PROPOSITO = pregunta1, PRESUPUESTO = pregunta2, ALMACENAMIENTO = pregunta3, RAM = pregunta4, CAMARA = pregunta5, BATERIA = pregunta6).values('ID_OPCIONES','NOMBRE')
    return list(opciones)
  # ? iPhone 11
  elif pregunta1 == 'Gamming y entretenimiento' and pregunta2 == '1.000.000$ - 2.000.000$' and pregunta3 == '64 GigaBytes' and pregunta4 == '4 GygaBytes' and pregunta5 == '12 Megapixeles' and pregunta6 == '3110 Mph':
    opciones = Opciones.objects.filter(PROPOSITO = pregunta1, PRESUPUESTO = pregunta2, ALMACENAMIENTO = pregunta3, RAM = pregunta4, CAMARA = pregunta5, BATERIA = pregunta6).values('ID_OPCIONES','NOMBRE')
    return list(opciones)
  # ? VIVO V25
  elif pregunta1 == 'Gamming y entretenimiento' and pregunta2 == '1.000.000$ - 2.000.000$' and pregunta3 == '128 GigaBytes' and pregunta4 == '8 GygaBytes' and pregunta5 == '64 Megapixeles' and pregunta6 == '4500 Mph':
    opciones = Opciones.objects.filter(PROPOSITO = pregunta1, PRESUPUESTO = pregunta2, ALMACENAMIENTO = pregunta3, RAM = pregunta4, CAMARA = pregunta5, BATERIA = pregunta6).values('ID_OPCIONES','NOMBRE')
    return list(opciones)
  # ? MOTOROLA Edge50 Neo
  elif pregunta1 == 'Gamming y entretenimiento' and pregunta2 == '1.000.000$ - 2.000.000$' and pregunta3 == '256 GigaBytes' and pregunta4 == '8 GygaBytes' and pregunta5 == '50 Megapixeles' and pregunta6 == '4400 Mph':
    opciones = Opciones.objects.filter(PROPOSITO = pregunta1, PRESUPUESTO = pregunta2, ALMACENAMIENTO = pregunta3, RAM = pregunta4, CAMARA = pregunta5, BATERIA = pregunta6).values('ID_OPCIONES','NOMBRE')
    return list(opciones)
  # ? iPhone 13 
  elif pregunta1 == 'Gamming y entretenimiento' and pregunta2 == '2.000.000$ - 3.000.000$' and pregunta3 == '128 GigaBytes' and pregunta4 == '6 GygaBytes' and pregunta5 == '12 Megapixeles' and pregunta6 == '3110 Mph':
    opciones = Opciones.objects.filter(PROPOSITO = pregunta1, PRESUPUESTO = pregunta2, ALMACENAMIENTO = pregunta3, RAM = pregunta4, CAMARA = pregunta5, BATERIA = pregunta6).values('ID_OPCIONES','NOMBRE')
    return list(opciones)
  # ? HONOR H200
  elif pregunta1 == 'Gamming y entretenimiento' and pregunta2 == '2.000.000$ - 3.000.000$' and pregunta3 == '256 GigaBytes' and pregunta4 == '12 GygaBytes' and pregunta5 == '50 Megapixeles' and pregunta6 == '5200 Mph':
    opciones = Opciones.objects.filter(PROPOSITO = pregunta1, PRESUPUESTO = pregunta2, ALMACENAMIENTO = pregunta3, RAM = pregunta4, CAMARA = pregunta5, BATERIA = pregunta6).values('ID_OPCIONES','NOMBRE')
    return list(opciones)
  # ? Xiaomi 14T
  elif pregunta1 == 'Gamming y entretenimiento' and pregunta2 == '2.000.000$ - 3.000.000$' and pregunta3 == '512 GigaBytes' and pregunta4 == '12 GygaBytes' and pregunta5 == '50 Megapixeles' and pregunta6 == '5000 Mph':
    opciones = Opciones.objects.filter(PROPOSITO = pregunta1, PRESUPUESTO = pregunta2, ALMACENAMIENTO = pregunta3, RAM = pregunta4, CAMARA = pregunta5, BATERIA = pregunta6).values('ID_OPCIONES','NOMBRE')
    return list(opciones)
  # ? iPhone 12
  elif pregunta1 == 'Gamming y entretenimiento' and pregunta2 == '3.000.000$ - 5.000.000$' and pregunta3 == '64 GigaBytes' and pregunta4 == '4 GygaBytes' and pregunta5 == '12 Megapixeles' and pregunta6 == '3110 Mph':
    opciones = Opciones.objects.filter(PROPOSITO = pregunta1, PRESUPUESTO = pregunta2, ALMACENAMIENTO = pregunta3, RAM = pregunta4, CAMARA = pregunta5, BATERIA = pregunta6).values('ID_OPCIONES','NOMBRE')
    return list(opciones)
  # ? iPhone 15
  elif pregunta1 == 'Gamming y entretenimiento' and pregunta2 == '3.000.000$ - 5.000.000$' and pregunta3 == '128 GigaBytes' and pregunta4 == '6 GygaBytes' and pregunta5 == '12 Megapixeles' and pregunta6 == '3877 Mph':
    opciones = Opciones.objects.filter(PROPOSITO = pregunta1, PRESUPUESTO = pregunta2, ALMACENAMIENTO = pregunta3, RAM = pregunta4, CAMARA = pregunta5, BATERIA = pregunta6).values('ID_OPCIONES','NOMBRE')
    return list(opciones)
  # ? HUAWEI P60 Pro
  elif pregunta1 == 'Gamming y entretenimiento' and pregunta2 == '3.000.000$ - 5.000.000$' and pregunta3 == '256 GigaBytes' and pregunta4 == '8 GygaBytes' and pregunta5 == '48 Megapixeles' and pregunta6 == '5800 Mph':
    opciones = Opciones.objects.filter(PROPOSITO = pregunta1, PRESUPUESTO = pregunta2, ALMACENAMIENTO = pregunta3, RAM = pregunta4, CAMARA = pregunta5, BATERIA = pregunta6).values('ID_OPCIONES','NOMBRE')
    return list(opciones)
  # ? SAMSUNG Galaxy S24FE
  elif pregunta1 == 'Gamming y entretenimiento' and pregunta2 == '3.000.000$ - 5.000.000$' and pregunta3 == '512 GigaBytes' and pregunta4 == '8 GygaBytes' and pregunta5 == '50 Megapixeles' and pregunta6 == '4500 Mph':
    opciones = Opciones.objects.filter(PROPOSITO = pregunta1, PRESUPUESTO = pregunta2, ALMACENAMIENTO = pregunta3, RAM = pregunta4, CAMARA = pregunta5, BATERIA = pregunta6).values('ID_OPCIONES','NOMBRE')
    return list(opciones)
  # ? iPhone 16 Pro
  elif pregunta1 == 'Gamming y entretenimiento' and pregunta2 == '5.000.000$ - MAS' and pregunta3 == '128 GigaBytes' and pregunta4 == '8 GygaBytes' and pregunta5 == '48 Megapixeles' and pregunta6 == '3900 Mph':
    opciones = Opciones.objects.filter(PROPOSITO = pregunta1, PRESUPUESTO = pregunta2, ALMACENAMIENTO = pregunta3, RAM = pregunta4, CAMARA = pregunta5, BATERIA = pregunta6).values('ID_OPCIONES','NOMBRE')
    return list(opciones)
  # ? Galaxy Z Flip6
  elif pregunta1 == 'Gamming y entretenimiento' and pregunta2 == '5.000.000$ - MAS' and pregunta3 == '256 GigaBytes' and pregunta4 == '12 GygaBytes' and pregunta5 == '50 Megapixeles' and pregunta6 == '4000 Mph':
    opciones = Opciones.objects.filter(PROPOSITO = pregunta1, PRESUPUESTO = pregunta2, ALMACENAMIENTO = pregunta3, RAM = pregunta4, CAMARA = pregunta5, BATERIA = pregunta6).values('ID_OPCIONES','NOMBRE')
    return list(opciones)
  # ? Galaxy Z Fold6
  elif pregunta1 == 'Gamming y entretenimiento' and pregunta2 == '5.000.000$ - MAS' and pregunta3 == '512 GigaBytes' and pregunta4 == '4 GygaBytes' and pregunta5 == '50 Megapixeles' and pregunta6 == '4500 Mph':
    opciones = Opciones.objects.filter(PROPOSITO = pregunta1, PRESUPUESTO = pregunta2, ALMACENAMIENTO = pregunta3, RAM = pregunta4, CAMARA = pregunta5, BATERIA = pregunta6).values('ID_OPCIONES','NOMBRE')
    return list(opciones)
  # ? HUAWEI Pura70 Ultra
  elif pregunta1 == 'Gamming y entretenimiento' and pregunta2 == '5.000.000$ - MAS' and pregunta3 == '512 GigaBytes' and pregunta4 == '16 GygaBytes' and pregunta5 == '50 Megapixeles' and pregunta6 == '5200 Mph':
    opciones = Opciones.objects.filter(PROPOSITO = pregunta1, PRESUPUESTO = pregunta2, ALMACENAMIENTO = pregunta3, RAM = pregunta4, CAMARA = pregunta5, BATERIA = pregunta6).values('ID_OPCIONES','NOMBRE')
    return list(opciones)
  #! RECOMENDACIONES PARA Durabilidad
  #? SAMSUNG Galaxy A05 
  if pregunta1 == 'Durabilidad' and pregunta2 == '100.000$ - 500.000$' and pregunta3 == '64 GigaBytes' and pregunta4 == '4 GygaBytes' and pregunta5 == '50 Megapixeles' and pregunta6 == '5000 Mph':
    opciones = Opciones.objects.filter(PROPOSITO = pregunta1, PRESUPUESTO = pregunta2, ALMACENAMIENTO = pregunta3, RAM = pregunta4, CAMARA = pregunta5, BATERIA = pregunta6).values('ID_OPCIONES','NOMBRE')
    return list(opciones)
  # ? XIAOMI REDMI 13C
  elif pregunta1 == 'Durabilidad' and pregunta2 == '100.000$ - 500.000$' and pregunta3 == '128 GigaBytes' and pregunta4 == '4 GygaBytes' and pregunta5 == '50 Megapixeles' and pregunta6 == '5000 Mph':
    opciones = Opciones.objects.filter(PROPOSITO = pregunta1, PRESUPUESTO = pregunta2, ALMACENAMIENTO = pregunta3, RAM = pregunta4, CAMARA = pregunta5, BATERIA = pregunta6).values('ID_OPCIONES','NOMBRE')
    return list(opciones)
  #? KALLEY BLACK Z
  elif pregunta1 == 'Durabilidad' and pregunta2 == '100.000$ - 500.000$' and pregunta3 == '256 GigaBytes' and pregunta4 == '6 GygaBytes' and pregunta5 == '50 Megapixeles' and pregunta6 == '5000 Mph':
    opciones = Opciones.objects.filter(PROPOSITO = pregunta1, PRESUPUESTO = pregunta2, ALMACENAMIENTO = pregunta3, RAM = pregunta4, CAMARA = pregunta5, BATERIA = pregunta6).values('ID_OPCIONES','NOMBRE')
    return list(opciones)
  # ? Celular TCL 50Pro
  elif pregunta1 == 'Durabilidad' and pregunta2 == '500.000$ - 1.000.000$' and pregunta3 == '512 GigaBytes' and pregunta4 == '8 GygaBytes' and pregunta5 == '108 Megapixeles' and pregunta6 == '5200 Mph':
    opciones = Opciones.objects.filter(PROPOSITO = pregunta1, PRESUPUESTO = pregunta2, ALMACENAMIENTO = pregunta3, RAM = pregunta4, CAMARA = pregunta5, BATERIA = pregunta6).values('ID_OPCIONES','NOMBRE')
    return list(opciones)
  # ?  HUAWEI Nova 10 SE
  elif pregunta1 == 'Durabilidad' and pregunta2 == '500.000$ - 1.000.000$' and pregunta3 == '128 GigaBytes' and pregunta4 == '8 GygaBytes' and pregunta5 == '108 Megapixeles' and pregunta6 == '4500 Mph':
    opciones = Opciones.objects.filter(PROPOSITO = pregunta1, PRESUPUESTO = pregunta2, ALMACENAMIENTO = pregunta3, RAM = pregunta4, CAMARA = pregunta5, BATERIA = pregunta6).values('ID_OPCIONES','NOMBRE')
    return list(opciones)
  # ? VIVO Y03 
  elif pregunta1 == 'Durabilidad' and pregunta2 == '500.000$ - 1.000.000$' and pregunta3 == '128 GigaBytes' and pregunta4 == '4 GygaBytes' and pregunta5 == '13 Megapixeles' and pregunta6 == '5000 Mph':
    opciones = Opciones.objects.filter(PROPOSITO = pregunta1, PRESUPUESTO = pregunta2, ALMACENAMIENTO = pregunta3, RAM = pregunta4, CAMARA = pregunta5, BATERIA = pregunta6).values('ID_OPCIONES','NOMBRE')
    return list(opciones)
  # ? iPhone 11
  elif pregunta1 == 'Durabilidad' and pregunta2 == '1.000.000$ - 2.000.000$' and pregunta3 == '64 GigaBytes' and pregunta4 == '4 GygaBytes' and pregunta5 == '12 Megapixeles' and pregunta6 == '3110 Mph':
    opciones = Opciones.objects.filter(PROPOSITO = pregunta1, PRESUPUESTO = pregunta2, ALMACENAMIENTO = pregunta3, RAM = pregunta4, CAMARA = pregunta5, BATERIA = pregunta6).values('ID_OPCIONES','NOMBRE')
    return list(opciones)
  # ? VIVO V25
  elif pregunta1 == 'Durabilidad' and pregunta2 == '1.000.000$ - 2.000.000$' and pregunta3 == '128 GigaBytes' and pregunta4 == '8 GygaBytes' and pregunta5 == '64 Megapixeles' and pregunta6 == '4500 Mph':
    opciones = Opciones.objects.filter(PROPOSITO = pregunta1, PRESUPUESTO = pregunta2, ALMACENAMIENTO = pregunta3, RAM = pregunta4, CAMARA = pregunta5, BATERIA = pregunta6).values('ID_OPCIONES','NOMBRE')
    return list(opciones)
  # ? MOTOROLA Edge50 Neo
  elif pregunta1 == 'Durabilidad' and pregunta2 == '1.000.000$ - 2.000.000$' and pregunta3 == '256 GigaBytes' and pregunta4 == '8 GygaBytes' and pregunta5 == '50 Megapixeles' and pregunta6 == '4400 Mph':
    opciones = Opciones.objects.filter(PROPOSITO = pregunta1, PRESUPUESTO = pregunta2, ALMACENAMIENTO = pregunta3, RAM = pregunta4, CAMARA = pregunta5, BATERIA = pregunta6).values('ID_OPCIONES','NOMBRE')
    return list(opciones)
  # ? iPhone 13 
  elif pregunta1 == 'Durabilidad' and pregunta2 == '2.000.000$ - 3.000.000$' and pregunta3 == '128 GigaBytes' and pregunta4 == '6 GygaBytes' and pregunta5 == '12 Megapixeles' and pregunta6 == '3110 Mph':
    opciones = Opciones.objects.filter(PROPOSITO = pregunta1, PRESUPUESTO = pregunta2, ALMACENAMIENTO = pregunta3, RAM = pregunta4, CAMARA = pregunta5, BATERIA = pregunta6).values('ID_OPCIONES','NOMBRE')
    return list(opciones)
  # ? HONOR H200
  elif pregunta1 == 'Durabilidad' and pregunta2 == '2.000.000$ - 3.000.000$' and pregunta3 == '256 GigaBytes' and pregunta4 == '12 GygaBytes' and pregunta5 == '50 Megapixeles' and pregunta6 == '5200 Mph':
    opciones = Opciones.objects.filter(PROPOSITO = pregunta1, PRESUPUESTO = pregunta2, ALMACENAMIENTO = pregunta3, RAM = pregunta4, CAMARA = pregunta5, BATERIA = pregunta6).values('ID_OPCIONES','NOMBRE')
    return list(opciones)
  # ? Xiaomi 14T
  elif pregunta1 == 'Durabilidad' and pregunta2 == '2.000.000$ - 3.000.000$' and pregunta3 == '512 GigaBytes' and pregunta4 == '12 GygaBytes' and pregunta5 == '50 Megapixeles' and pregunta6 == '5000 Mph':
    opciones = Opciones.objects.filter(PROPOSITO = pregunta1, PRESUPUESTO = pregunta2, ALMACENAMIENTO = pregunta3, RAM = pregunta4, CAMARA = pregunta5, BATERIA = pregunta6).values('ID_OPCIONES','NOMBRE')
    return list(opciones)
  # ? iPhone 12
  elif pregunta1 == 'Durabilidad' and pregunta2 == '3.000.000$ - 5.000.000$' and pregunta3 == '64 GigaBytes' and pregunta4 == '4 GygaBytes' and pregunta5 == '12 Megapixeles' and pregunta6 == '3110 Mph':
    opciones = Opciones.objects.filter(PROPOSITO = pregunta1, PRESUPUESTO = pregunta2, ALMACENAMIENTO = pregunta3, RAM = pregunta4, CAMARA = pregunta5, BATERIA = pregunta6).values('ID_OPCIONES','NOMBRE')
    return list(opciones)
  # ? iPhone 15
  elif pregunta1 == 'Durabilidad' and pregunta2 == '3.000.000$ - 5.000.000$' and pregunta3 == '128 GigaBytes' and pregunta4 == '6 GygaBytes' and pregunta5 == '12 Megapixeles' and pregunta6 == '3877 Mph':
    opciones = Opciones.objects.filter(PROPOSITO = pregunta1, PRESUPUESTO = pregunta2, ALMACENAMIENTO = pregunta3, RAM = pregunta4, CAMARA = pregunta5, BATERIA = pregunta6).values('ID_OPCIONES','NOMBRE')
    return list(opciones)
  # ? HUAWEI P60 Pro
  elif pregunta1 == 'Durabilidad' and pregunta2 == '3.000.000$ - 5.000.000$' and pregunta3 == '256 GigaBytes' and pregunta4 == '8 GygaBytes' and pregunta5 == '48 Megapixeles' and pregunta6 == '5800 Mph':
    opciones = Opciones.objects.filter(PROPOSITO = pregunta1, PRESUPUESTO = pregunta2, ALMACENAMIENTO = pregunta3, RAM = pregunta4, CAMARA = pregunta5, BATERIA = pregunta6).values('ID_OPCIONES','NOMBRE')
    return list(opciones)
  # ? SAMSUNG Galaxy S24FE
  elif pregunta1 == 'Durabilidad' and pregunta2 == '3.000.000$ - 5.000.000$' and pregunta3 == '512 GigaBytes' and pregunta4 == '8 GygaBytes' and pregunta5 == '50 Megapixeles' and pregunta6 == '4500 Mph':
    opciones = Opciones.objects.filter(PROPOSITO = pregunta1, PRESUPUESTO = pregunta2, ALMACENAMIENTO = pregunta3, RAM = pregunta4, CAMARA = pregunta5, BATERIA = pregunta6).values('ID_OPCIONES','NOMBRE')
    return list(opciones)
  # ? iPhone 16 Pro
  elif pregunta1 == 'Durabilidad' and pregunta2 == '5.000.000$ - MAS' and pregunta3 == '128 GigaBytes' and pregunta4 == '8 GygaBytes' and pregunta5 == '48 Megapixeles' and pregunta6 == '3900 Mph':
    opciones = Opciones.objects.filter(PROPOSITO = pregunta1, PRESUPUESTO = pregunta2, ALMACENAMIENTO = pregunta3, RAM = pregunta4, CAMARA = pregunta5, BATERIA = pregunta6).values('ID_OPCIONES','NOMBRE')
    return list(opciones)
  # ? Galaxy Z Flip6
  elif pregunta1 == 'Durabilidad' and pregunta2 == '5.000.000$ - MAS' and pregunta3 == '256 GigaBytes' and pregunta4 == '12 GygaBytes' and pregunta5 == '50 Megapixeles' and pregunta6 == '4000 Mph':
    opciones = Opciones.objects.filter(PROPOSITO = pregunta1, PRESUPUESTO = pregunta2, ALMACENAMIENTO = pregunta3, RAM = pregunta4, CAMARA = pregunta5, BATERIA = pregunta6).values('ID_OPCIONES','NOMBRE')
    return list(opciones)
  # ? Galaxy Z Fold6
  elif pregunta1 == 'Durabilidad' and pregunta2 == '5.000.000$ - MAS' and pregunta3 == '512 GigaBytes' and pregunta4 == '4 GygaBytes' and pregunta5 == '50 Megapixeles' and pregunta6 == '4500 Mph':
    opciones = Opciones.objects.filter(PROPOSITO = pregunta1, PRESUPUESTO = pregunta2, ALMACENAMIENTO = pregunta3, RAM = pregunta4, CAMARA = pregunta5, BATERIA = pregunta6).values('ID_OPCIONES','NOMBRE')
    return list(opciones)
  # ? HUAWEI Pura70 Ultra
  elif pregunta1 == 'Durabilidad' and pregunta2 == '5.000.000$ - MAS' and pregunta3 == '512 GigaBytes' and pregunta4 == '16 GygaBytes' and pregunta5 == '50 Megapixeles' and pregunta6 == '5200 Mph':
    opciones = Opciones.objects.filter(PROPOSITO = pregunta1, PRESUPUESTO = pregunta2, ALMACENAMIENTO = pregunta3, RAM = pregunta4, CAMARA = pregunta5, BATERIA = pregunta6).values('ID_OPCIONES','NOMBRE')
    return list(opciones)
  
  return [25, 'LO SIENTO NO PUEDO AYUDARTE']