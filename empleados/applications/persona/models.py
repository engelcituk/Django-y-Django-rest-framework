from django.db import models
#importacion del modelo con que estará relacionado nuestra tabla de empleados
from applications.departamento.models import Departamento


# Modelo para la tabla empleado.
class Empleado(models.Model):

    job_choices = (
        ('0','Contador'),
        ('1','Administrador'),
        ('2','Economista'),
        ('3','Otro')        
    )

    #el id para pk no es necesario definirlo, puesto que django internamente lo hace
    first_name = models.CharField('Nombres', max_length=60) #Nombres, asi lo verá el admin de django
    last_name = models.CharField('Apellidos', max_length=60) #Apellidos, asi lo verá el admin de django
    job = models.CharField('Trabajo', max_length=50, choices=job_choices) 
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE) #columna de relacion con la tabla Departamento
    #image = models.ImageField(, upload_to=None, height_field=None, width_field=None, max_length=None)

    def __str__(self):
        return str( self.id ) + '-' + self.first_name + ' ' + self.last_name 