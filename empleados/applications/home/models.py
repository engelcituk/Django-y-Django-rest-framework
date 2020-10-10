from django.db import models

# Create your models here.
class Prueba(models.Model):
    titulo = models.CharField(max_length=100)
    subtitulo = models.CharField(max_length=50)
    cantidad = models.IntegerField()

    def __str__(self):
        return self.titulo + ' ' + self.subtitulo #aparentemente solo regresa titulo mas subtitulo, pero desde nuestro template se puede acceder a todo el modelo