from django.shortcuts import render
from rest_framework import generics, viewsets

from . import models, serializers
from ..base.permissions  import IsAuthor


class GenreView(generics.ListAPIView):
    """List of genres"""

    queryset = models.Genre.objects.all()

    serializers_class = serializers.GenreSerializer 



class LicenseView(viewsets.ModelViewSet):
    """CRUD licenses of authors"""

    serializer_class = serializers.LicenseSerializer
    permission_classes = [IsAuthor]

    def get_queryset(self   ):
        return models.License.objects.filter(user=self.request.user)
    

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)