from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status, generics, filters
from rest_framework.response import Response
from django.contrib.auth.models import User
from .serializers import UserSerializer
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAdminUser, AllowAny
import django_filters.rest_framework
# Create your views here.
class UserList(generics.ListCreateAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer
	permission_classes = (AllowAny,)