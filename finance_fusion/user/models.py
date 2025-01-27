from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import BaseUserManager


# Create your models here.
class CustomUserManager(BaseUserManager):
     def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        extra_fields.setdefault('is_active', True)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

     def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if not extra_fields.get('is_staff'):
            raise ValueError('Superuser must have is_staff=True')

        if not extra_fields.get('is_superuser'):
            raise ValueError('Superuser must have is_superuser=True')
        
        return self.create_user(email, password, **extra_fields) 

class CustomUser(AbstractUser):
    username = None
    middle_name = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(unique=True,db_index=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()
    
    def __str__(self):
        return self.email

