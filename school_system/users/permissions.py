# from rest_framework import permissions


# class AdminPermission(permissions.BasePermission):

#     def has_permission(self, request, view):
#         if request.method in permissions.SAFE_METHODS:
#             return True
#         return request.user.is_admin or request.user.is_superuser


# class TeacherPermission(permissions.BasePermission):

#     def has_add_permission(self, request, view):
#         if request.method in permissions.SAFE_METHODS:
#             return True
#         if not request.user.is_authenticated:
#             return False
#         return request.user.is_authenticated and request.user.is_teacher

#     def has_delete_permission(self, request, view):
#         if request.method in permissions.SAFE_METHODS:
#             return True
#         if not request.user.is_authenticated:
#             return False
#         return request.user.is_authenticated and request.user.is_teacher
