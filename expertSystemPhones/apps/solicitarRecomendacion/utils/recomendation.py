from apps.solicitarRecomendacion.models import Opciones
def recomendation_phone(pregunta1, pregunta2, pregunta3, pregunta4, pregunta5, pregunta6):
  sugerencias = Opciones.objects.filter(PROPOSITO = pregunta1,
                                        PRESUPUESTO = pregunta2,
                                        ALMACENAMIENTO = pregunta3,
                                        RAM = pregunta4,
                                        CAMARA = pregunta5,
                                        BATERIA = pregunta6
                                        ).values('ID_OPCIONES','NOMBRE')
  return sugerencias