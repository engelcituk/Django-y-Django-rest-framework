from django.shortcuts import render
from django.views.generic import (ListView, TemplateView, CreateView) 
#importo el modelo empleado
from .models import Empleado

class ListaEmpleados(ListView):
    template_name = "empleado/lista.html"
    model = Empleado #para asignarle un nombre de variable al queryset que se pasaran al template
    context_object_name = 'empleados' #para asignarle un nombre de variable al queryset que se pasaran al template


