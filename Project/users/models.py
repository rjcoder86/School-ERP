from django.db import models
from django.contrib.auth.models import  AbstractBaseUser
from .managers import BaseUserManager, CustomUserManager
from study.models import Subject


class User(AbstractBaseUser):
    full_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    profile_pic = models.CharField(max_length=50, null=True)
    contact = models.CharField(max_length=13)

    USERNAME_FIELD:str = 'email'
    REQUIRED_FIELDS:list = ["email"]

    objects = CustomUserManager()

    def get_email(self):
        return self.email

class Teacher(User):
    guardian = models.CharField(max_length=50)
    emergency_contact = models.CharField(max_length=13)
    bloodGroup = models.CharField(max_length=3)
    subjects = models.ManyToManyField(Subject) 

    class Meta:
        verbose_name_plural = "Teacher"

class Parent(User):

    class Meta:
        verbose_name_plural = "Parent"
class Student(User):
    guardian = models.ForeignKey(Parent, on_delete= models.CASCADE, null=True, blank=True)
    emergency_contact = models.CharField(max_length=13)
    bloodGroup = models.CharField(max_length=3)
    subjects = models.ManyToManyField(Subject)
    class Meta:
        verbose_name_plural = "Student"
