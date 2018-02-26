from django.db import models
from django.utils import timezone
# Create your models here.
class User(models.Model):
    user_name = models.CharField(max_length=250)
    user_email = models.CharField(max_length=250, unique=True)
    user_organization = models.CharField(max_length=250)
    user_password = models.CharField(max_length=250)
    is_related = models.BooleanField()
    is_doctor = models.BooleanField()
    is_admin = models.BooleanField(default=False)
    add_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.user_name + " log in " +  str(self.add_at)

class Question(models.Model):   
    name = models.CharField(max_length=250)
    answer = models.CharField(max_length=250)
    add_at = models.DateTimeField(auto_now=True)
    update_at = models.DateTimeField(auto_now=True)

class AddLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    add_at = models.DateTimeField()


class QuizLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    create_at =  models.DateTimeField(auto_now=True)

class QuizDetail(models.Model):
    quizLog = models.ForeignKey(QuizLog, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    detail = models.CharField(max_length=250)
