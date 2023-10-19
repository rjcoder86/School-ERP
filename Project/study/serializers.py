from rest_framework.serializers import ModelSerializer
from . models import *

class SubjectSerializer(ModelSerializer):
    class meta:
        model = Subject
        field = '__all__'

class QuestionsSerializer(ModelSerializer):
    class meta:
        model = Questions
        field = '__all__'

class TestSerializer(ModelSerializer):
    class meta:
        model = Test
        field = '__all__'

class ResultSerializer(ModelSerializer):
    class meta:
        model = Result
        field = '__all__'