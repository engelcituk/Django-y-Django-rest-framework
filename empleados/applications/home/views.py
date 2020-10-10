from django.shortcuts import render
# vistas genericas
from django.views.generic import TemplateView, ListView

# Create your views here.
class PruebaView(TemplateView):
    template_name = 'home/prueba.html'


class PruebaListView(ListView):
    # model = MODEL_NAME
    template_name = "home/lista.html"
    context_object_name = 'listaNumeros' #para asignarle un nombre de variable al queryset que se pasaran al template
    queryset = [1,2,3,4,5,6,7,8,9]
  