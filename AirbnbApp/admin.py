from django.contrib import admin
from .models.user import User
from .models.account import Account
from .models.reserva import  Reserva
from .models.ubicacion import Ubicacion
#from .plan import Plan
#from .tipo_plan import Tipo_plan
#from .tipo_plan_restriccion import  Tipo_plan_restriccion
#from .restriccion import Restriccion
#from .detalle_tipo_plan import Detalle_tipo_plan

admin.site.register(User)
admin.site.register(Account)
admin.site.register(Reserva)
admin.site.register(Ubicacion)
#admin.site.register(Plan)
#admin.site.register(Tipo_plan)
#admin.site.register(Tipo_plan_restriccion)
#admin.site.register(Restriccion)
#admin.site.register(Detalle_tipo_plan)
# Register your models here.
