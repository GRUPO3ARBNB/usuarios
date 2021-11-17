from django.db import models

class Ubicacion(models.Model):
    id_ubicacion = models.AutoField(primary_key=True)
    nombre = models.CharField('nombre', max_length=50)
    latitud = models.CharField('latitud', max_length=80)
    longitud = models.CharField('longitud', max_length=80)
    municipio = models.CharField('municipio', max_length=50)
    departamento = models.CharField('departamento', max_length=50)
    pais = models.CharField('pais', max_length=50)
    fecha_creacion = models.CharField('fecha_creacion', max_length=50)
