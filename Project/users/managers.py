from django.contrib.auth.models import UserManager as BaseUserManager
from common_utils.enums import UserTypes

class CustomUserManager(BaseUserManager):
    def _create_user(self, email:str, password:str, **extra_fields):
        if not email:
            raise ValueError("Email field should be provided")

        email = self.normalize_email(email=email).lower()
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    
    def create_user(self, email:str, password:str, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_admin', False)

        return self._create_user(email=email, password=password, **extra_fields)

    
    def create_superuser(self, email:str, password:str, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_admin', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_admin') is not True:
            raise ValueError('Superuser must have is_admin=True.')

        return self._create_user(email=email, password=password, **extra_fields)