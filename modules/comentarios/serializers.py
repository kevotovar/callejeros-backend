from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Comentario

class ComentarioSerializer(serializers.ModelSerializer):
	class Meta:
		model = Comentario
		fields=('id_comentario','id_usuario','id_mascota','comentario','created')