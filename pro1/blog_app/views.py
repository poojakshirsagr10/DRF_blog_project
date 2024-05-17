from django.shortcuts import render
from .serializers import BlogListSerializer,BlogCreateSerializer,BlogDeleteSerializer,BlogUpdateSerializer
from .models import Blog
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView
from rest_framework.permissions import IsAuthenticated,BasePermission,SAFE_METHODS
from .permissions import IsOwnerOrReadOnly
# Create your views here.
class BlogAPI(ListCreateAPIView):
    serializer_class = BlogCreateSerializer
    queryset = Blog.objects.all()
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return BlogListSerializer
        return BlogCreateSerializer


class BlogUpdateAPI(UpdateAPIView,RetrieveAPIView):
    serializer_class = BlogUpdateSerializer
    queryset = Blog.objects.all()
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsOwnerOrReadOnly]

class BlogDeleteAPI(DestroyAPIView):
    serializer_class = BlogDeleteSerializer
    queryset = Blog.objects.all()
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsOwnerOrReadOnly]
