from rest_framework import serializers
from ..models import CustomUser

# class loginSerializer(ModelSerializer):
#     class Meta:
#         model = CustomUser
#         fields = ['email', 'password']
#         extra_kwargs = {'password': {'write_only': True}}

class LoginSerializer(serializers.Serializer):
    email =serializers.EmailField()
    password = serializers.CharField()