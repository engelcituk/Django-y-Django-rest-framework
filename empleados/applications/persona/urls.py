from django.contrib import admin
from django.urls import path
from . import views  # con el . se indica que está en el mismo nivel de la carpeta


urlpatterns = [
    path('empleados/', views.ListaEmpleados.as_view() ),  
    path('empleadosporarea/', views.ListaEmpleadosPorArea.as_view() ),    

]