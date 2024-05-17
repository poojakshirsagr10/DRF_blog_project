from django.shortcuts import render
from rest_framework import viewsets
from .serializers import UserSerializer,User



# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()


