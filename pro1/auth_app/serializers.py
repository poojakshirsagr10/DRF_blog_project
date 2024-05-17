from django.contrib.auth.models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username','password','email')

    def create(self, validated_data):
        obj = User.objects.create_user(**validated_data)
        return obj
