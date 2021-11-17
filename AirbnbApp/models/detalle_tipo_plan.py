"""from django.db import models
from django.db.models.base import ModelStateFieldsCacheDescriptor
from .plan import Plan
from .tipo_plan import Tipo_plan

class Detalle_tipo_plan(models.Model):
    id_detalle_tipo_plan=models.CharField(primary_key=True)
    id_plan=models.ForeignKey(Plan, related_name="plan", on_delete=models.CASCADE)
    id_tipo_plan=models.ForeignKey(Tipo_plan, related_name="tipo_plan", on_delete=models.CASCADE)"""
