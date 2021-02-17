import jwt

from rest_framework import status
from rest_framework.generics import ListAPIView, GenericAPIView
from rest_framework.response import Response

from rest_framework_simplejwt.tokens import RefreshToken

from .serializers import LoginSerializer, UserSerializer, RegisterSerializer
from .models import User


class ProfileView(ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def get_queryset(self):
        return self.queryset.filter(id=self.request.user.id)


class RegisterView(GenericAPIView):

    serializer_class = RegisterSerializer

    def post(self, request):
        user = request.data
        serializer = self.serializer_class(data=user)

        serializer.is_valid(raise_exception=True)
        serializer.save()

        user_data = serializer.data
        user = User.objects.get(username=user_data["username"])

        token = RefreshToken.for_user(user).access_token
        return Response(user_data, status=status.HTTP_201_CREATED)


class LoginView(GenericAPIView):

    serializer_class = LoginSerializer

    def post(self, request):

        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
