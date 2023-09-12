from rest_framework.serializers import ModelSerializer
from .models import Student,Parent, Teacher

class StudentSerializer(ModelSerializer):

    class Meta:
        model = Student
        fields = ['full_name', 'email','profile_pic', 'contact', 'guardian','emergency_contact','bloodGroup']

class ParentSerializer(ModelSerializer):

    class Meta:
        model = Parent
        fields = ['full_name', 'email','profile_pic', 'contact']

class TeacherSerializer(ModelSerializer):

    class Meta:
        model = Teacher
        fields = ['full_name', 'email','profile_pic', 'contact', 'guardian','emergency_contact','bloodGroup']