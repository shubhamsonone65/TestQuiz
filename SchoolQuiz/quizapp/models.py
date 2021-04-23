from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Question(models.Model):
    category_choices = [
        ('computer', 'computer'),
        ('GK', 'GK'),
        ('animals', 'animals'),
        ('geography', 'geography'),
        ('history', 'history'),
    ]
    que = models.CharField(max_length=500)
    Correctop = models.CharField(max_length=100)
    wrongop1 = models.CharField(max_length=100)
    wrongop2 = models.CharField(max_length=100)
    wrongop3 = models.CharField(max_length=100)
    category = models.CharField(choices=category_choices,max_length=9)
    desc=models.CharField(max_length=500)

    def __str__(self):
        return 'Question id:'+str(self.id)

class student(models.Model):
    studentacc=models.ForeignKey(User, on_delete=models.CASCADE)
    email=models.CharField(max_length=100)
    record=models.TextField()

    def __str__(self):
        return 'student : '+self.studentacc.username

class Quiz(models.Model):
    student=models.ForeignKey(student, on_delete=models.CASCADE)
    record=models.TextField()
    score=models.IntegerField()
    time=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "QuizId : "+str(self.id)+" solved by "+self.student.studentacc.username

