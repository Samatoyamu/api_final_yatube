from rest_framework import permissions

UNSAFE_METHODS = ('PUT', 'PATCH', 'DELETE')


class CanPost(permissions.BasePermission):
    message = 'Только пользователи могут оставлять комментарий или посты!'

    def has_permission(self, request, view):
        if request.method == 'POST':
            return request.user.is_authenticated
        return True


class IsAuthor(permissions.BasePermission):
    message = 'Изменение,удаление чужого контента запрещено!'

    def has_object_permission(self, request, view, obj):
        if request.method in UNSAFE_METHODS:
            return obj.author == request.user
        return True
