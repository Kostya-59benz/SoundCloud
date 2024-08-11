from rest_framework import viewsets, parsers, permissions

from .. import serializer

class UserView(viewsets.ModelViewSet):

    parser_classes = (parsers.MultiPartParser,)
    serializer_class = serializer.UserSerilizer

    permission_classes =  [permissions.IsAuthenticated]


    def get_queryset(self):
        print(self.request.user)
        return self.request.user
    

    def get_object(self):
        print(self.get_queryset())
        return self.get_queryset()
    

