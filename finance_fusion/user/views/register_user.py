from ..serializer.user_register import CustomUserListSerializer, CustomUserCreateSerializer, SuperUserCreateSerializer
from rest_framework import generics
from ..models import CustomUser
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated
from ..permissions.Is_superuser import IsSuperUser

class CustomUserListCreate(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    # permission_classes = [AllowAny]
    
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CustomUserCreateSerializer
        return CustomUserListSerializer
    
    def get_permissions(self):
        if self.request.method == 'POST':
            return [AllowAny()]
        return [IsAuthenticated()]

    
class SuperuserListCreate(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsSuperUser]
    serializer_class = SuperUserCreateSerializer    