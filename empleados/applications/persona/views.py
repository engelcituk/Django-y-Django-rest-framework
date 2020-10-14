from django.shortcuts import render
from django.views.generic import (ListView, TemplateView, CreateView) 
#importo el modelo empleado
from .models import Empleado

class ListaEmpleados(ListView):
    template_name = "empleado/lista.html"
    paginate_by = 4 #paginacion, en la url se pondría por get los sig ?page=3
    model = Empleado 
    context_object_name = 'empleados' 

class ListaEmpleadosPorArea(ListView):
    template_name = "empleado/listaPorArea.html"
    model = Empleado 
    """ queryset = Empleado.objects.filter(
        departamento__shor_name = 'TICS' 
    )"""
    context_object_name = 'empleados' 

    def get_queryset(self):
        
        area = self.kwargs['area'] #para recoger la variable que se envia como parametro en la url-> empleadosporarea/<area>'
        lista = Empleado.objects.filter(
            departamento__shor_name = area #campoDelModeloEmpleadosConRelacionMuchosAmuchos____nombre_del_campo_del_modelo_relacionado_con_empleado
        )
        return lista

class ListaEmpleadosPorKword(ListView):
    #lista de empleados por palabra clave
    template_name = "empleado/porKword.html"
    model = Empleado 
    context_object_name = 'empleados'

    def get_queryset(self):
        #para filtrar en base a lo que se recibe desde una caja de texto
        keyword = self.request.GET.get("kword", '')

        lista = Empleado.objects.filter(
            first_name = keyword 
        )
        return lista       