from ..serializer.user_login import LoginSerializer
from rest_framework import generics
from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate, login,logout
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status 
from rest_framework.response import Response


class Loginview(generics.GenericAPIView):
    permission_classes = [AllowAny]
    serializer_class = LoginSerializer

    def post(self,request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = authenticate(
                email = serializer.validated_data['email'],
                password = serializer.validated_data['password']
            )
            if user is not None:
                login(request,user)
                refresh_token = RefreshToken.for_user(user=user)
                access_token = refresh_token.access_token
                response = {
                    "access_token": str(access_token),
                    "refresh_token": str(refresh_token)
                }
                return Response(response, status=status.HTTP_200_OK)
            return Response({"message":"Invalid Credentials"}, status=status.HTTP_400_BAD_REQUEST)