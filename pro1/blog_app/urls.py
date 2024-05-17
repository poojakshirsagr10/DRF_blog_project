from django.urls import path
from .views import BlogAPI,BlogUpdateAPI,BlogDeleteAPI

urlpatterns=[
    path('blogs/',BlogAPI.as_view()),
    path('blogs/<pk>/',BlogUpdateAPI.as_view()),
    path('blogs/del/<pk>/',BlogDeleteAPI.as_view())
]