from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    """Checks if the user is the object owner."""
    def has_object_permission(self, request, view, obj):
        return obj.autor == request.user


class IsUser(BasePermission):
    """Only allows the owner."""
    def has_object_permission(self, request, view, obj):
        return request.user and request.user == obj
