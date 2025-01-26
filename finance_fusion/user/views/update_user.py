from ..models import CustomUser
from ..serializers.user_register import CustomUserDetailSerializer
from rest_framework import generics
from rest_framework import permissions
from rest_framework_simplejwt import authentication


class CustomUserDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserDetailSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.JWTAuthentication]
    lookup_field = 'id'
    