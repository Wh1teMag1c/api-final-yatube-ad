"""Права доступа для API."""

from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    """Разрешение доступа только автору контента для редактирования."""

    def has_object_permission(self, request, view, obj):
        """Проверка прав на уровне объекта."""
        return (
                request.method in permissions.SAFE_METHODS
                or obj.author == request.user
        )
