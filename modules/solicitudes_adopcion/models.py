from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Solicitud_adopcion(models.Model):
	 id_solicitud = models.AutoField(primary_key=True)
	 id_usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='solicitudes')
	 id_mascota = models.ForeignKey('mascotas.Mascota')
	 created = models.DateTimeField(auto_now_add = True)
	 updated = models.DateTimeField(auto_now = True) 