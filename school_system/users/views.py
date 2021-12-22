from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.views import APIView

from .permissions import AdminPermission


class DeleteAccount(APIView):
    permission_classes = [AdminPermission]

    def delete(self, request, *args, **kwargs):
        user = request.user
        user.delete()
        return Response({"result": "user delete"})
