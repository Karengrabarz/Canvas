from rest_framework.permissions import SAFE_METHODS, BasePermission

from .models import Course


class IsSuperuserOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS: 
            return True
        return request.user.is_superuser and request.user.is_authenticated
    # def has_permission(self, request, view):
    #     return request.method in SAFE_METHODS