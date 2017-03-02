from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Comentario(models.Model):
	id_comentario = models.AutoField(primary_key=True)
	id_usuario = models.ForeignKey(User, on_delete=models.CASCADE,related_name="comentarios")
	id_mascota = models.ForeignKey('mascotas.Mascota')
	comentario = models.CharField(max_length=500)
	created = models.DateTimeField(auto_now_add = True)
	updated = models.DateTimeField(auto_now = True)