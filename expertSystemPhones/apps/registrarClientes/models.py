from django.db import models

# Create your models here.
class Cliente(models.Model):
  ID_CLIENTE = models.AutoField(primary_key=True)
  NOMBRES = models.CharField(max_length=255)
  APELLIDOS = models.CharField(max_length=255)
  CORREO = models.EmailField(max_length=255)


  class Meta:
    db_table = 'CLIENTE'



class Pregunta(models.Model):
  ID_PREGUNTAS = models.AutoField(primary_key=True)
  PREGUNTA = models.CharField(max_length=255)


  class Meta:
    db_table = 'PREGUNTAS'

  def __str__(self):
    return self.PREGUNTA
  

class Respuesta(models.Model):
  ID_RESPUESTAS = models.AutoField(primary_key=True)
  ID_PREGUNTAS = models.ForeignKey(Pregunta, on_delete=models.CASCADE,  db_column='ID_PREGUNTAS')
  RESPUESTA = models.CharField(max_length=255)


  class Meta:
    db_table = 'RESPUESTAS'

  def __str__(self):
    return self.RESPUESTA