from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.template import loader
# Create your views here.

def index(request):
    return HttpResponse('<h1>Bienvenidos a mi pagina de django</h1>')

def plantilla(request):
    
    template = loader.get_template('plantilla.html')

    datos = {
        'lista': ['primero', 'segundo', 'tercero'],
        'nombre': 'Juancho',
        'apellido': 'Fort'
    }

    plantilla_generada = template.render(datos)
    
    return HttpResponse(plantilla_generada)