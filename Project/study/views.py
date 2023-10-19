from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from .permissions import IsTeacher
from .models import Subject, Questions, Result, Test

# Create your views here.
class Subjects(APIView):
    permission_classes = [IsTeacher,]

    def get(self,request):
        subjcets = Subjects.objects.all()

    def post(self, request):
        pass

class Questions(APIView):
    permission_classes = [IsAuthenticated,]

    def get(self,request):
        pass

    def post(self, request):
        pass

    