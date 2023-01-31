from rest_framework import permissions


class CanPost(permissions.BasePermission):
    message = 'Создайте аккаунт или войдите, чтобы постить или комментировать!'

    def has_permission(self, request, view):
        if request.method == 'POST':
            return request.user.is_authenticated
        return True


class IsAuthor(permissions.BasePermission):
    message = 'Изменение,удаление чужого контента запрещено!'

    def has_object_permission(self, request, view, obj):
        return (request.method in permissions.SAFE_METHODS
                or obj.author == request.user)
