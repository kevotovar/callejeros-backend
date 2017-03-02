from rest_framework.views import APIView
from rest_framework import status, generics, filters
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser, AllowAny
from django.shortcuts import get_object_or_404
import django_filters.rest_framework
from django.contrib.auth.models import User
from .models import Solicitud_adopcion
from .serializers import SolicitudSerializer
# Create your views here.

class SolicitudesList(generics.ListCreateAPIView):
	queryset = Solicitud_adopcion.objects.all()
	serializer_class = SolicitudSerializer
	permissions_classes = (AllowAny,)
