from django.contrib import admin
from .models import Empleado, Habilidades

# Register your models here.
admin.site.register(Habilidades)

#django en los models son trae el valor que _self indica, en este punto se modifica para indicar los campos mostrar en una tabla del administrador django
class EmpleadoAmin(admin.ModelAdmin):
    #list_display -> columnas a mostrar del modelo    
    list_display = (
        'id',
        'first_name',
        'last_name',
        'departamento',
        'job',
        'full_name' #full_name-> campo perzonalizado, no existe en el modelo, por lo que se debe crear una funcion que retorna el valor que se pretenda que muestre
    )
    #search_fields-> buscador por first_name last_name
    search_fields = (
        'first_name',
        'last_name',
    )
    #Funcion para llenar el campo personalizado full_name 
    def full_name(self, obj):
        return obj.first_name + ' ' + obj.last_name

    #list_filter-> para agregar un filtro, en la tabla
    list_filter = ('departamento','job','habilidades',)
    #filter_horizontal-> filtro horizontal, que sirve para los campos de relacion muchos a muchos, al registrar un empleado
    filter_horizontal = ('habilidades',)

admin.site.register(Empleado, EmpleadoAmin)
