from django.shortcuts import render, redirect
from django.contrib import messages
from ReservaDjandoApp.forms import FormReserva
from ReservaDjandoApp.models import Reserva

# Create your views here.

def index(request):
    return render(request, 'index.html')

def listarReservas (request):
    
    reservas = Reserva.objects.all()
    data = {'reservas': reservas}
    return render(request, 'reservas.html', data )

def agregarReserva (request):
    form = FormReserva()

    if(request.method == 'POST'):
        form = FormReserva(request.POST)
        if(form.is_valid()):
            messages.success(request, 'La reserva se ha agregado correctamente.')            
            form.save()
            return index(request)
        else:
            for field, errors in form.errors.items():
                    for error in errors:
                        messages.error(request, f'Error en el campo {field}: {error}')
    
    data = { 'form' : form}
    return render(request, 'agregar.html', data)

def eliminarReserva (request, id_req):
    
    reserva = Reserva.objects.get(idReserva = id_req)
    reserva.delete()

    return redirect('/reservas')

def modificarReserva (request, id_req):
    
    reserva = Reserva.objects.get(idReserva = id_req)    
    form = FormReserva(instance=reserva)

    if(request.method == 'POST'):
        form = FormReserva(request.POST, instance = reserva)
        if(form.is_valid()):
            form.save()
            return index(request)

    data = { 'form' : form}
    return render(request, 'agregar.html', data)
