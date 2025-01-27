from rest_framework import serializers
from ..models import Transaction
from django.contrib.auth import get_user_model

User = get_user_model()

class UserForTransactionListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'middle_name', 'last_name']

class TranscationListSerializer(serializers.ModelSerializer):
    user = UserForTransactionListSerializer()
    class Meta:
        model = Transaction
        fields = ['id','user','amount','month']
