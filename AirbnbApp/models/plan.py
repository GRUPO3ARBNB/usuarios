"""from django.db import models
from django.db.models.base import ModelStateFieldsCacheDescriptor
from .ubicacion import Ubicacion

class Plan (models.Model):
    id_plan = models.CharField (primary_key=True, max_length=20)
    id_ubicacion = models.ForeignKey (Ubicacion, related_name='ubicacion', on_delete=models.CASCADE)
    nombre =models.CharField('nombre', max_length=20)
    descripcion = models.CharField('descripcion', max_length=500)
    precio_dia = models.CharField('precio_dia', max_length=30)
    capacidad = models.CharField('capacidad', max_length=20)
    fecha_creacion = models.DateField
    activo = models.BooleanField"""
