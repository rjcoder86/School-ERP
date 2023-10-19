from rest_framework.permissions import BasePermission
from users.models import Teacher, Student, Parent

class IsTeacher(BasePermission):
    """
    Allows access only to Teachers.
    """

    def has_permission(self, request, view):
        return bool(request.user and isinstance(request.user, Teacher))