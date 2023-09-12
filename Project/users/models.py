from django.db import models
from django.contrib.auth.models import User


class Teacher(User):
    full_name = models.CharField(max_length=50)
    contact = models.CharField(max_length=13)
    guardian = models.CharField(max_length=50)
    emergency_contact = models.CharField(max_length=13)
    bloodGroup = models.CharField(max_length=3)
    profile_pic = models.CharField(max_length=50)
    # subjects = models.ManyToMany(Subject, on_delete=CASCADE) To be added when Subject model completed.


class Student(User):
    full_name = models.CharField(max_length=50)
    contact = models.CharField(max_length=13)
    guardian = models.CharField(max_length=50)
    emergency_contact = models.CharField(max_length=13)
    bloodGroup = models.CharField(max_length=3)
    profile_pic = models.CharField(max_length=50)
    # subjects = models.ManyToMany(Subject, on_delete=CASCADE) To be added when Subject model completed.
    # standard = models.CharField(max_length=10)


class Parents(User):
    full_name = models.CharField(max_length=50)
    contact = models.CharField(max_length=13)   
    profile_pic = models.CharField(max_length=50)

