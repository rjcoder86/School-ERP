from django.db import models
from common_utils.enums import QuestionTypes
from users.models import Teacher, Student

# Create your models here.
class Subject(models.Model):
    name = models.CharField(max_length=100)
    reference_books = models.JSONField()

class Question(models.Model):
    question = models.JSONField()
    """ 
     Format  -> 
     {
        question: description of question,
        options: {
        a: "", b:"",.....
        }
     }
    """
    answer = models.CharField(max_length=512)
    answer_explaination = models.CharField(max_length=256, null=True, blank=True)
    author = models.ForeignKey(Teacher, on_delete= models.CASCADE)
    type = models.SmallIntegerField(choices=QuestionTypes.choices())
    marks = models.CharField(max_length=10)

class Test(models.Model):
    name = models.CharField(max_length=200)
    subject = models.ForeignKey(Subject,on_delete=models.CASCADE)
    questions = models.ManyToManyRel(Question, related_name="tests", related_query_name="test")
    total_time = models.TimeField()
    total_marks = models.CharField(max_length=10)
    author = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)

class TestAttempt(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    examiniee = models.ForeignKey(Student, on_delete= models.CASCADE) 
    answers = models.JSONField()
    """
    [{Question id: PKID, AttemptedAnswer:"AnswerByStudent"}, {}, {}, ....]
    """
    aquired_marks = models.CharField(max_length=10)
