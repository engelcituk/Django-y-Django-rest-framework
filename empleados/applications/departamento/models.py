from django.db import models

# Create your models here.
class Departamento(models.Model):
    #el id para pk no es necesario definirlo, puesto que django internamente lo hace
    name = models.CharField('Nombre', max_length=50, blank=True) #Nombre, asi lo verá el admin de django
    shor_name = models.CharField('Nombre corto', max_length=20, unique=True) #Nombre corto, asi lo verá el admin de django
    anulate = models.BooleanField('Anulado',default=False)#Anulado, asi lo verá el admin de django y por defecto falso

    def __str__(self):
        return str( self.id ) + '-' + self.name + ' ' + self.shor_name 