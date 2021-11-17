"""from django.db import models
from django.db.models.base import ModelStateFieldsCacheDescriptor
from tipo_plan import Tipo_plan
from restriccion import restriccion

class   Tipo_plan_restriccion(models.Model):
    id_tipo_plan_resticcion = models.CharField(primary_key=True)
    id_tipo_plan = models.ForeignKey(tipo_plan, related_name='tipo_plan',on_delete=models.CASCADE)
    id_restriccion = models.ForeignKey(restriccion, related_name='restriccion',on_delete=models.CASCADE)"""
