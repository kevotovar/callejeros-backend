from rest_framework.views import APIView
from rest_framework import status, generics, filters
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser, AllowAny, IsAuthenticatedOrReadOnly
from django.shortcuts import get_object_or_404
import django_filters.rest_framework
from django.contrib.auth.models import User
from .models import Mascota, Raza, Especie
from .serializers import MascotaSerializer, RazaSerializer, EspecieSerializer
from .permissions import IsOwnOrReadOnly



# Create your views here.
class MascotasList(generics.ListCreateAPIView):
	queryset=Mascota.objects.all()
	serializer_class=MascotaSerializer
	permission_classes=(IsAuthenticatedOrReadOnly,)
	

class RazasList(generics.ListCreateAPIView):
	queryset = Raza.objects.all()
	serializer_class = RazaSerializer
	permission_classes=(IsAuthenticatedOrReadOnly,)

class EspeciesList(generics.ListCreateAPIView):
	queryset = Especie.objects.all()
	serializer_class = EspecieSerializer
	permission_classes=(IsAuthenticatedOrReadOnly,)
