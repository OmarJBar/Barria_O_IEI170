from django.shortcuts import render, redirect
from django import forms
from ReservaDjandoApp.forms import reservaForms

# Create your views here.

def index(request):
    return render(request, 'index.html')


def filterNumPerson (request):
    
    numPersons = request.POST.get('numeroPersonas')

    if(numPersons <1 or numPersons >15):
        return render(request, 'mi_template.html', {'error_message': "El número de personas debe estar entre 1 y 15"})

    return numPersons
