from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

User = get_user_model()  # Refers to our custom User model

class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for User model during registration.
    Handles creation with password hashing, email-based auth.
    """
    password = serializers.CharField(write_only=True, required=True)  # Hide password in responses

    class Meta:
        model = User
        fields = ['id', 'email', 'password', 'first_name', 'last_name']  # Username not included
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        """
        Create user using custom manager's create_user method.
        No username required, as handled by CustomUserManager.
        """
        user = User.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password'],
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', '')
        )
        return user

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    """
    Custom serializer for login to use email instead of username.
    """
    username_field = 'email'  # Use email for authentication

    def validate(self, attrs):
        """
        Override to add custom logic if needed (e.g., extra user data in token).
        """
        data = super().validate(attrs)
        return data
