from rest_framework import permissions
from rest_framework.permissions import IsAdminUser


class AnusPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.id == 3

class PenisPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return bool(request.user.is_staff)