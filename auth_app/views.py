from auth_app.models import User
from auth_app.serializers import UserSerializer, LoginSerializer

from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import AllowAny

from django.contrib.auth import authenticate, login, logout
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_protect

# Create your views here.


class BaseCommonViewSet(ModelViewSet):
    queryset = None
    serializer_class = None

    def create(self, request, *args, **kwargs):
        return Response({'detail': 'This method is not allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def list(self, request, *args, **kwargs):
        return Response({'detail': 'This method is not allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def retrieve(self, request, *args, **kwargs):
        return Response({'detail': 'This method is not allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def update(self, request, *args, **kwargs):
        return Response({'detail': 'This method is not allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def partial_update(self, request, *args, **kwargs):
        return Response({'detail': 'This method is not allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def destroy(self, request, *args, **kwargs):
        return Response({'detail': 'This method is not allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


@method_decorator(ensure_csrf_cookie, name='dispatch')
class CSRFTokenViewSet(BaseCommonViewSet):
    permission_classes = [AllowAny]

    def list(self, request):
        return Response({'detail': 'CSRF cookie set'}, status=status.HTTP_200_OK)


@method_decorator(csrf_protect, name='dispatch')
class UserRegistrationViewSet(BaseCommonViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
            serializer.create(serializer.validated_data)
            return Response('New user has been created', status=status.HTTP_201_CREATED)
        except ValidationError as validationError:
            return Response(validationError.detail, status=status.HTTP_400_BAD_REQUEST)


@method_decorator(csrf_protect, name='dispatch')
class UserLoginViewSet(BaseCommonViewSet):
    queryset = User.objects.all()
    serializer_class = LoginSerializer
    permission_classes = [AllowAny]

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
            email = serializer.validated_data.get('email')
            password = serializer.validated_data.get('password')
            user = authenticate(email=email, password=password)
            if user:
                login(request, user)
                return Response('User has been logged in', status=status.HTTP_200_OK)
            return Response('Invalid credentials', status=status.HTTP_401_UNAUTHORIZED)
        except ValidationError as validationError:
            return Response(validationError.detail, status=status.HTTP_400_BAD_REQUEST)


class UserLogoutViewSet(BaseCommonViewSet):
    queryset = User.objects.all()
    serializer_class = LoginSerializer
    permission_classes = [AllowAny]

    # user logout request here
    def list(self, request, *args, **kwargs):
        logout(request)
        return Response('User has been logged out', status=status.HTTP_200_OK)
