from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Ubicacion(models.Model):
	id_ubicacion=models.AutoField(primary_key=True)
	id_usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ubicaciones')
	calle=models.CharField(max_length=100)
	num_ext=models.IntegerField()
	num_int=models.IntegerField()
	colonia=models.CharField(max_length=100)
	ciudad=models.CharField(max_length=100)
	estado=models.CharField(max_length=100)
	cp=models.IntegerField()
	created = models.DateTimeField(auto_now_add = True)
	updated = models.DateTimeField(auto_now = True)

class Telefono(models.Model):
	id_telefono=models.AutoField(primary_key=True)
	id_usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='telefonos')
	numero =models.IntegerField()
	created = models.DateTimeField(auto_now_add = True)
	updated = models.DateTimeField(auto_now = True)

class Donativo(models.Model):
	id_donativo=models.AutoField(primary_key=True)
	id_usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='donativos')
	monto = models.IntegerField()
	created = models.DateTimeField(auto_now_add = True)
	updated = models.DateTimeField(auto_now = True)
