from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Mascota, Especie, Raza, Foto_mascota

class FotosMascotasSerializer(serializers.ModelSerializer):
	class Meta:
		model = Foto_mascota
		fields=('id_foto','url_foto','created')

class MascotaSerializer(serializers.ModelSerializer):
	fotos = FotosMascotasSerializer(read_only=True,many=True)
	#rescatista = serializers.StringRelatedField()
	class Meta:
		model = Mascota
		fields = ('id_especie','id_raza','nombre','rescatista','sexo','edad','status','fotos','created')

class RazaSerializer(serializers.ModelSerializer):
	class Meta:
		model = Raza
		fields = ('id_raza','raza')

class EspecieSerializer(serializers.ModelSerializer):
	class Meta:
		model = Especie
		fields = ('id_especie','especie')