from django import forms
from django.core import validators 
from ReservaDjandoApp.models import Reserva

class FormReserva(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = '__all__'

    ESTADOS = [('activo', 'ACTIVO'), ('inactivo', 'INACTIVO'), ('bloquedo', 'BLOQUEADO')]

    fechaReserva = forms.DateField(widget=forms.SelectDateWidget())
    estado = forms.CharField(widget=forms.Select(choices=ESTADOS))
    nombrePersona = forms.CharField()


    def filterByCantidadPersonas(self):
        inputCantidadPersons = self.cleaned_data['numeroPersonas']
        if inputCantidadPersons < 1 or inputCantidadPersons > 15:
            raise forms.ValidationError("El numero de personas no es el esperado...")
        return inputCantidadPersons
    
    def filterByNombrePersonas(self):
        inputnombrePersona = self.cleaned_data['nombrePersona']
        if len(inputnombrePersona) > 80:
            raise forms.ValidationError("El nombre excede el maximo")
        return inputnombrePersona
    
    estado.widget.attrs['class'] = 'form-select'