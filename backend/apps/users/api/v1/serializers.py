"""API serializers"""

# Django rest F.
from rest_framework import serializers

# models
from apps.users.models import User


class UserSerializer(serializers.ModelSerializer):
    """Model user serializer"""

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')


class ChangePasswordSerializer(serializers.Serializer):
    """Change password serializer"""
    password = serializers.CharField(max_length=128)
    confirm_password = serializers.CharField(max_length=128)

    def validate(self, data):
        if not data['password'] or not data['confirm_password']:
            raise serializers.ValidationError("Please enter a password and "
                                              "confirm it.")
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError("Those passwords don't match.")
        return data
