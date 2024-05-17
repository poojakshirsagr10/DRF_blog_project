from rest_framework import serializers
from .models import Blog

class BlogCreateSerializer(serializers.ModelSerializer):
    blog_created_by = serializers.HiddenField(default=serializers.CurrentUserDefault())

    created_at = serializers.DateTimeField( read_only=True)
    class Meta:
        model = Blog
        exclude = ['updated_at']

class BlogListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = "__all__"

class BlogUpdateSerializer(serializers.ModelSerializer):
    updated_field = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Blog
        exclude = ['created_at']

class BlogDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = "__all__"






