from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an task to edit it.
    """

    def has_object_permission(self, request, view, obj):
        # allow all read methods
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the owner of the task.
        return obj.customer.id == request.user.customer.id

