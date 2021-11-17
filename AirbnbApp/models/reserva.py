from django.db import models
from django.db.models.base import ModelStateFieldsCacheDescriptor
from .user import User
#from .plan import Plan

class Reserva (models.Model):
    id_reserva = models.CharField (primary_key=True, max_length=20)
    id_user = models.ForeignKey (User, related_name='user', on_delete=models.CASCADE)
    #id_plan = models.ForeignKey (Plan, related_name='plan', on_delete=models.CASCADE)
    cantidad_personas =models.CharField('cantidad_personas', max_length=20)
    fecha_registro = models.DateField
    fecha_desde = models.DateField
    fecha_hasta = models.DateField
