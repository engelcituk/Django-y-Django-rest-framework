from django.contrib import admin
from .models import Empleado, Habilidades
# Register your models here.
admin.site.register(Habilidades)

#django en los models son trae el valor que _self indica, en este punto se modifica para indicar los campos mostrar en una tabla del administrador django
class EmpleadoAmin(admin.ModelAdmin):
    #columnas a mostrar del modelo    
    list_display = (
        'first_name',
        'last_name',
        'departamento',
        'job',
    )
    #buscador por first_name last_name
    search_fields = (
        'first_name',
        'last_name',
    )
    #para agregar un filtro, en la tabla
    list_filter = ('job','habilidades',)
    #filtro horizontal, que sirve para los campos de relacion muchos a muchos, al registrar un empleado
    filter_horizontal = ('habilidades',)

admin.site.register(Empleado, EmpleadoAmin)
