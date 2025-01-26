from serializers.user_register import CustomUserListSerializer, CustomUserCreateSerializer, SuperUserCreateSerializer
from rest_framework import generics
from ..models import CustomUser
from rest_framework.permissions import AllowAny

class CustomUserListCreate(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    permission_classes = [AllowAny]
    
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CustomUserCreateSerializer
        return CustomUserListSerializer
    
class SuperuserListCreate(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    permission_classes = [AllowAny]
    serializer_class = SuperUserCreateSerializer    