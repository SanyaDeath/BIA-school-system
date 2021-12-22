from django.contrib.auth import get_user_model
from djoser.serializers import UserCreateSerializer

# from rest_framework import serializers

User = get_user_model()


class UserRegistrationSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ('email', 'username', 'last_name', 'first_name',
                  'middle_name', 'birth_date', 'klass', 'password')
