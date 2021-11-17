from AirbnbApp.models.reserva import Reserva
from AirbnApp.models.users import User
from rest_framework import serializers

class ReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserva
        fields = (id_reserva, id_user, cantidad_personas, fecha_registro, fecha_desde, fecha_hasta)

    def create(self, validated_data):

        reservaInstance = Reserva.objects.create(**validated_data)
        return reservaInstance

    def to_representation(self, obj):
        reserva = Reserva.objects.get(id_reserva=obj.id_reserva)
        return{
            'idReserva': reserva.id_reserva,
            'idUser': reserva.id_user,
            'cantidadPersonas': reserva.cantidad_personas,
            'fechaRegistro': reserva.fecha_registro,
            'fechaDesde': reserva.fecha_desde,
            'fechaHasta': reserva.fecha_hasta
        }
