from django.contrib import admin
from .models import Mascota, Raza, Especie

class MascotaAdmin(admin.ModelAdmin):
	pass

admin.site.register(Mascota, MascotaAdmin)

class RazaAdmin(admin.ModelAdmin):
	pass

admin.site.register(Raza, RazaAdmin)

class EspecieAdmin(admin.ModelAdmin):
	pass

admin.site.register(Especie, EspecieAdmin)
