# models.py
from django.db import models

class Curso(models.Model):
    nombre = models.CharField(max_length=200)
    fecha_inicio = models.DateField()
    plazas_disponibles = models.IntegerField()
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre
