from rest_framework import permissions

class CustomPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        print(request.user, request.user.is_authenticated )
        return request.user and request.user.is_authenticated