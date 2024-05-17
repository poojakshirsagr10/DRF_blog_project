from django.db import models

# Create your models here
from django.db import models
from django.contrib.auth.models import User


class Blog(models.Model):
    title = models.CharField(max_length=20)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    CATEGORY_CHOICE = [('science','science'),('history','history'),('geography','geography'),('other','other')]
    category = models.CharField(max_length=10, choices = CATEGORY_CHOICE, default='other')
    blog_created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="created_blog" )
