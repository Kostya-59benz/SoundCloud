from rest_framework import viewsets, parsers, permissions

from .. import serializer


class UserView(viewsets.ModelViewSet):

    parser_classes = (parsers.MultiPartParser,)
    serializer_class = serializer.UserSerilizer

    permission_classes =  []


    def get_queryset(self):
        return self.request.user
    

    def get_object(self):
        return self.get_queryset()
    

