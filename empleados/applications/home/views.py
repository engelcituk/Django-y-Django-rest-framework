from django.shortcuts import render
# vistas genericas
from django.views.generic import TemplateView

# Create your views here.
class PruebaView(TemplateView):
    template_name = 'home/prueba.html'