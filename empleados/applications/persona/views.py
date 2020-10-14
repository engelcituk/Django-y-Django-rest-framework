from django.shortcuts import render
from django.views.generic import (ListView, TemplateView, CreateView) 
#importo el modelo empleado
from .models import Empleado

class ListaEmpleados(ListView):
    template_name = "empleado/lista.html"
    model = Empleado 
    context_object_name = 'empleados' 

class ListaEmpleadosPorArea(ListView):
    template_name = "empleado/listaPorArea.html"
    model = Empleado 
    queryset = Empleado.objects.filter(
        departamento__shor_name = 'TICS' 
    )
    context_object_name = 'empleados' 


