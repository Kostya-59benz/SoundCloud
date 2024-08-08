from rest_framework import serializers


class GoogleAuth(serializers.Serializer):
    """ Сериализация даних от Google"""

    email = serializers.EmailField()
    token = serializers.CharField()