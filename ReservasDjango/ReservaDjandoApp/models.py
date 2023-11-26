from django.db import models

# Create your models here.

class Reserva(models.Model):
    idReserva = models.IntegerField()
    nombrePersona = models.CharField(max_length=50)
    fono = models.IntegerField()
    fechaReserva = models.DateField()
    numeroPersonas = models.IntegerField()
    correo = models.CharField(max_length=50)
    estado = models.CharField(max_length=50)
    observacion = models.CharField(max_length=50)