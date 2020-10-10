from django.contrib import admin
from django.urls import path
from . import views  # con el . se indica que está en el mismo nivel de la carpeta


urlpatterns = [
    path('prueba/', views.PruebaView.as_view() ),
    path('lista/', views.PruebaListView.as_view() ),

]