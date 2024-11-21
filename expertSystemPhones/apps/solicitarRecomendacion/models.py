from django.db import models
from apps.registrarClientes.models import Cliente

# Create your models here.
class Hechos(models.Model):
  ID_HECHOS = models.AutoField(primary_key=True)
  NOMBRE = models.CharField(max_length=255)
  
  class Meta:
    db_table = 'HECHOS'

class Opciones(models.Model):
  ID_OPCIONES = models.AutoField(primary_key=True)
  PROPOSITO = models.CharField(max_length=255)
  PRESUPUESTO = models.CharField(max_length=255)
  ALMACENAMIENTO = models.CharField(max_length=255)
  RAM = models.CharField(max_length=255)
  CAMARA = models.CharField(max_length=255)
  BATERIA = models.CharField(max_length=255)
  NOMBRE = models.CharField(max_length=255)

  class Meta:
    db_table = 'OPCIONES'


class HechosXOpciones (models.Model):
  ID_HECHOSXOPCIONES = models.AutoField(primary_key=True)
  ID_HECHOS_FK = models.ForeignKey(Hechos, on_delete = models.CASCADE)
  ID_OPCIONES_FK = models.ForeignKey(Opciones, on_delete = models.CASCADE)

  class Meta:
    db_table = 'HECHOSXOPCIONES'


class Recomendacion(models.Model):
  ID_RECOMENDACION = models.AutoField(primary_key=True)
  FECHA = models.DateField(auto_now_add=True)
  ID_CLIENTE_FK = models.ForeignKey(Cliente, on_delete=models.CASCADE)

  class Meta:
    db_table = 'RECOMENDACION'




class RecomendacionXOpciones(models.Model):
  ID_RECOMENDACIONXOPCIONES = models.AutoField(primary_key=True)
  ID_OPCIONES_FK = models.ForeignKey(Opciones, on_delete = models.CASCADE)
  ID_RECOMENDACION_FK = models.ForeignKey(Recomendacion, on_delete= models.CASCADE)


  class Meta:
    db_table = 'RECOMENDACIONXOPCIONES'