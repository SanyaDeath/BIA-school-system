from rest_framework import serializers

from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'role',
            'last_name',
            'first_name',
            'middle_name',
            'birth_date',
        )


class StudentSerializer(UserSerializer):
    class Meta:
        model = User
        fields = (
            'entry_year',
            'klass',
        )
