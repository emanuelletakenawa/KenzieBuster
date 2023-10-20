from rest_framework import permissions
from rest_framework.views import Request, View
from users.models import User


class AdminPermission(permissions.BasePermission):
    def has_object_permission(self, req: Request, view: View, user: User):
        return bool(req.user == user or req.user.is_superuser)
