from django.shortcuts import render
from rest_framework import viewsets

from taskapi.models import User
from taskapi.serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer