from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Solicitud_adopcion

class SolicitudSerializer(serializers.ModelSerializer):
	class Meta:
		model = Solicitud_adopcion
		fields = ('id_solicitud','id_usuario','id_mascota','created')