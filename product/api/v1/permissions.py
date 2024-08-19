from rest_framework.permissions import BasePermission, SAFE_METHODS
from users.models import Subscription


def make_payment(request):
    # TODO
    pass


class IsStudentOrIsAdmin(BasePermission):
    def has_permission(self, request, view):
        # Проверка, аутентифицирован ли пользователь
        if not request.user.is_authenticated:
            return False
        # Проверка, является ли пользователь администратором или студентом
        return request.user.is_staff or not request.user.is_staff

    def has_object_permission(self, request, view, obj):
        # Проверка, аутентифицирован ли пользователь
        if not request.user.is_authenticated:
            return False
        # Проверка, является ли пользователь администратором или студентом
        return request.user.is_staff or not request.user.is_staff


class ReadOnlyOrIsAdmin(BasePermission):

    def has_permission(self, request, view):
        return request.user.is_staff or request.method in SAFE_METHODS

    def has_object_permission(self, request, view, obj):
        return request.user.is_staff or request.method in SAFE_METHODS
