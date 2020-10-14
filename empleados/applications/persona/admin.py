from django.contrib import admin
from .models import Empleado, Habilidades
# Register your models here.
admin.site.register(Habilidades)

#django en los models son trae el valor que _self indica, en este punto se modifica para agregar más campos mostrar 
class EmpleadoAmin(admin.ModelAdmin):
    list_display = (
        'first_name',
        'last_name',
        'departamento',
        'job',
    )
admin.site.register(Empleado,EmpleadoAmin)
