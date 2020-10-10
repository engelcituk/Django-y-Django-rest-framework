from django.shortcuts import render
# vistas genericas
#al poner las importaciones en parentesis de pueden hacer saltos de linea
from django.views.generic import (TemplateView, ListView, CreateView) 
from .models import Prueba #importo el modelo 


# Create your views here.
class PruebaView(TemplateView):
    template_name = 'home/prueba.html'


class PruebaListView(ListView):
    # model = MODEL_NAME
    template_name = "home/lista.html"
    context_object_name = 'listaNumeros' #para asignarle un nombre de variable al queryset que se pasaran al template
    queryset = [1,2,3,4,5,6,7,8,9]


class ListarPrueba(ListView):
    template_name = "home/listaPrueba.html"
    model = Prueba
    context_object_name = 'lista' #para asignarle un nombre de variable al queryset que se pasaran al template

#para el template generico createview se requiere el parametro field para los campos que corresponde al modelo
class CreateViewPrueba(CreateView):
    template_name = "home/create.html"
    model = Prueba
    fields = ['titulo','subtitulo', 'cantidad']
