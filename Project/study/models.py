from django.db import models
from common_utils.enums import QuestionTypes

# Create your models here.
class Subject(models.Model):
    name = models.CharField(max_length=100)
    reference_books = models.JSONField()

class Questions(models.Model):
    question = models.CharField(max_length=300)
    type = models.SmallIntegerField(choices=QuestionTypes.choices(), null=True, blank=True)
    marks = models.CharField(max_length=10)

class Test(models.Model):
    name = models.CharField(max_length=200)
    subject = models.ForeignKey(Subject,on_delete=models.CASCADE)
    questions = models.JSONField()
    created_date = models.DateTimeField(auto_now_add=True)

class Result(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    answers = models.JSONField()
    marks = models.CharField(max_length=10)
