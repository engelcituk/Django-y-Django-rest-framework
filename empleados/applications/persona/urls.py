from django.contrib import admin
from django.urls import path
from . import views  # con el . se indica que está en el mismo nivel de la carpeta


urlpatterns = [
    path('empleados/', views.ListaEmpleados.as_view() ),  
    path('empleadosporarea/<area>', views.ListaEmpleadosPorArea.as_view() ),    
    path('empleadosporkword/', views.ListaEmpleadosPorKword.as_view() ),    
    path('empleadosporhabilidades/', views.ListaHabilidadesEpleado.as_view() ),    
    path('empleado/<pk>', views.EmpleadodetailView.as_view() ), #pk hace referencia al id del empleado   
    path('addempleado/', views.EmpleadoCreateView.as_view() ), #pk hace referencia al id del empleado   


]