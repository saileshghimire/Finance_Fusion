from rest_framework import serializers
from ..models import CustomUser

class CustomUserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)  # password is required but write-only

    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'middle_name', 'email', 'password']  # Define the fields explicitly

    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data) 
        return user
    

class CustomUserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields  = ['id', 'first_name', 'last_name', 'middle_name', 'email', 'is_active','is_staff', 'is_superuser']

class CustomUserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'first_name', 'last_name', 'middle_name', 'email', 'is_active','is_staff', 'is_superuser']
        extra_kwargs = {
            'is_staff': {'read_only': True},
            'is_superuser': {'read_only': True}
        }
    
    def update(self, instance, validated_data):
        user = self.context['request'].user

        if user.is_superuser or user.id == instance.id:
            for key, value in validated_data.items():
                setattr(instance, key, value)
            instance.save()
            return instance
        else:
            raise PermissionError('You do not have permission to update this user')
    


class SuperUserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)  

    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'middle_name', 'email', 'password', 'is_staff', 'is_superuser']  
        extra_kwargs = {
            'middle_name': {'required': False} 
        }


    def create_superuser(self, validated_data):
        user = CustomUser.objects.create_superuser(**validated_data) 
        return user