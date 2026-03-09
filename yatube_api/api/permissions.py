"""Права доступа для API приложения Yatube."""
from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    """Разрешение только автору редактировать объект."""

    def has_object_permission(self, request, view, obj):
        """Проверка прав на уровне объекта."""
        return (
            request.method in permissions.SAFE_METHODS
            or obj.author == request.user
        )
