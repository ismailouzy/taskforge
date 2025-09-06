from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from .serializers import UserSerializer, CustomTokenObtainPairSerializer
from .tasks import send_welcome_email  # Import Celery task

@method_decorator(csrf_exempt, name='dispatch')
class RegisterView(APIView):
    """
    API view for user registration.
    Allows anyone (no auth required) to create a new user.
    """
    permission_classes = [AllowAny]  # Open to all for signup

    def post(self, request):
        """
        Handle POST request to register user.
        """
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()  # Create user
            send_welcome_email.delay(user.email)  # Trigger async Celery task
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(TokenObtainPairView):
    """
    API view for user login.
    Uses custom serializer to return JWT tokens.
    """
    serializer_class = CustomTokenObtainPairSerializer
