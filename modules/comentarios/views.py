from rest_framework.views import APIView
from rest_framework import status,generics, filters
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser, AllowAny,IsAuthenticated
from django.shortcuts import get_object_or_404
import django_filters.rest_framework
from django.contrib.auth.models import User
from .models import Comentario
from .serializers import ComentarioSerializer
# Create your views here.

class ComentariosList(generics.ListCreateAPIView):
	queryset=Comentario.objects.all()
	serializer_class = ComentarioSerializer
	permissions_classes = (IsAuthenticated,)
