from rest_framework import serializers
from .models import AuthUser


class UserSerilizer(serializers.ModelSerializer):
    
    class Meta:
        model = AuthUser
        fields = ('avatar', 'country', 'city', 'bio', 'display_name')


class GoogleAuth(serializers.Serializer):
    """ Сериализация даних от Google"""

    email = serializers.EmailField()
    token = serializers.CharField()