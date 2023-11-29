from django.db import models

# Create your models here.

class Reserva(models.Model):
    idReserva = models.AutoField(primary_key=True)
    nombrePersona = models.CharField(max_length=80 , blank=False)
    fono = models.IntegerField(blank=False)
    fechaReserva = models.DateField(blank=False)
    numeroPersonas = models.IntegerField(blank=False)
    correo = models.EmailField(max_length=50 , blank=False)
    estado = models.CharField(max_length=50 , blank=False)
    observacion = models.CharField(max_length=50, blank=True)