from rest_framework import serializers

from . import models


class BaseSerializer(serializers.ModelSerializer):


    id = serializers.IntegerField()



class GenreSerializer(BaseSerializer):
    class Meta:
        model = models.Genre
        fields = ('id', 'name')



class LicenseSerializer(BaseSerializer):
    class Meta:
        model = models.License
        fields = ('id', 'name')