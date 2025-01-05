from rest_framework import permissions
from rest_framework.permissions import BasePermission


class CheckPatient(BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.user_role == 'patient'

class CheckSelf(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user == obj:
            return True
        return False