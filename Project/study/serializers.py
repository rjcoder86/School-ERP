from rest_framework.serializers import ModelSerializer
from . models import Subject, Question, Test, TestAttempt

class SubjectSerializer(ModelSerializer):
    class meta:
        model = Subject
        field = '__all__'

class QuestionsSerializer(ModelSerializer):
    class meta:
        model = Question
        field = '__all__'

class TestSerializer(ModelSerializer):
    class meta:
        model = Test
        field = '__all__'

class TestAttemptSerializer(ModelSerializer):
    class meta:
        model = TestAttempt
        field = '__all__'