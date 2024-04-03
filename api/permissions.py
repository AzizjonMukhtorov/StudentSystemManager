from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import BasePermission


class IsTeacher(BasePermission):
    msg = {'msg': 'Only teacher and admin can do this'}

    def has_permission(self, request, view):
        if request.user.is_authenticated and request.is_teacher:
            return True
        raise PermissionDenied(self.msg)


