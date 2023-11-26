from django import forms
from ReservaDjandoApp.models import Reserva

class FormReserva (forms.ModelForm):
  class meta:
      model = Reserva
      fields = '__all__'

