from AirbnbApp.models.ubicacion import ubicacion
from rest_framework import  serializers

class UbicacionSerializer(serializers.ModelSerializer):
    class Meta:
        model =ubicacion
        fields = [ 'nombre', 'latitud', 'longitud', 'municipio', 'departamento', 'pais', 'fecha_creacion'] 
