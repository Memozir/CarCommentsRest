from rest_framework.permissions import BasePermission


class CommentPermission(BasePermission):

    def has_permission(self, request, view):
        if view.action in ('list', 'retrieve', 'create'):
            return True
        else:
            return False
