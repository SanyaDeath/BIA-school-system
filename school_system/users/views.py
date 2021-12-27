# from rest_framework import mixins, viewsets

# from .models import Student, User
# from .permissions import TeacherPermission
# from .serializers import StudentSerializer, UserSerializer


# class CustomViewSet(
#     mixins.CreateModelMixin,
#     mixins.DestroyModelMixin,
#     mixins.ListModelMixin,
#     viewsets.GenericViewSet,
# ):
#     pass


# class UserViewSet(CustomViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     permission_classes = [TeacherPermission]
#     search_fields = ['last_name', 'first_name', 'middle_name']
