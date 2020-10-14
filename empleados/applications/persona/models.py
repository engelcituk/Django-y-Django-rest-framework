from django.db import models
from ckeditor.fields import RichTextField #importa ckeditor
#importacion del modelo con que estará relacionado nuestra tabla de empleados
from applications.departamento.models import Departamento

class Habilidades(models.Model):
    habilidad = models.CharField('Habilidad', max_length=50)

    class Meta:
        verbose_name = 'Habilidad'
        verbose_name_plural = 'Habilidades empleados'

    def __str__(self):
        return str( self.id ) + '-' + self.habilidad 

class Empleado(models.Model): # Modelo para la tabla empleado.

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
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE) #columna de relacion con la tabla Departamento, relacion de 1 a muchos
    #avatar = models.ImageField(upload_to='empleado', blank=True, null=True)
    habilidades = models.ManyToManyField(Habilidades)
    hoja_vida = RichTextField() 

    class Meta:
        verbose_name = 'Mi empleado'
        verbose_name_plural = 'Empleados de la empresa'
        ordering = ['first_name','last_name'] #se ordena por el campo name
        #ordering = ['-name'] #se ordena por el campo name, de la z a la a
        unique_together = ('first_name' , 'last_name') # valida que no se pueda generar registros con la combinacion entre 'first_name' y 'last_name'

    def __str__(self):
        return str( self.id ) + '-' + self.first_name + ' ' + self.last_name 