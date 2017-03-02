from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Foto_mascota(models.Model):
	id_foto=models.AutoField(primary_key=True)
	id_mascota=models.ForeignKey('Mascota')
	url_foto=models.CharField(max_length=250)
	created = models.DateTimeField(auto_now_add = True)
	updated = models.DateTimeField(auto_now = True)

class Raza(models.Model):
	id_raza = models.AutoField(primary_key=True)
	raza =models.CharField(max_length=100)

class Especie(models.Model):
	id_especie = models.AutoField(primary_key=True)
	especie = models.CharField(max_length=100)


class Mascota(models.Model):
	id_mascota = models.AutoField(primary_key=True)
	id_especie = models.ForeignKey('Especie')
	rescatista = models.ForeignKey(User, on_delete=models.CASCADE, related_name='mascotas')
	id_raza = models.ForeignKey('Raza')
	nombre = models.CharField(max_length=100)
	sexo = models.CharField(max_length=100)
	edad = models.CharField(max_length= 100)
	status = models.BooleanField(default=0)
	created = models.DateTimeField(auto_now_add = True)
	updated = models.DateTimeField(auto_now = True)