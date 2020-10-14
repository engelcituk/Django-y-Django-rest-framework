from django.db import models

# Create your models here.
class Departamento(models.Model):
    #el id para pk no es necesario definirlo, puesto que django internamente lo hace
    name = models.CharField('Nombre', max_length=50, blank=True) #Nombre, asi lo verá el admin de django
    shor_name = models.CharField('Nombre corto', max_length=20, unique=True) #Nombre corto, asi lo verá el admin de django
    anulate = models.BooleanField('Anulado',default=False)#Anulado, asi lo verá el admin de django y por defecto falso

    class Meta:
        verbose_name = 'Mi departamento'
        verbose_name_plural = 'Áreas de la empresa'
        ordering = ['name'] #se ordena por el campo name
        #ordering = ['-name'] #se ordena por el campo name, de la z a la a
        #unique_together = ('name' , 'shor_name') # valida que no se pueda generar registros con la combinacion entre 'name' y 'shor_name'



    def __str__(self):
        return str( self.id ) + '-' + self.name + ' ' + self.shor_name 