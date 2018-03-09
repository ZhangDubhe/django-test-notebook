from django.db import models
from django.utils import timezone
# Create your models here.


class User(models.Model):
    user_name = models.CharField(max_length=250)
    user_email = models.CharField(max_length=250, unique=True)
    user_password = models.CharField(max_length=250)
    is_admin = models.BooleanField(default=False)
    add_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.user_name + " create at" + str(self.add_at)


class Question(models.Model):   
    name = models.CharField(max_length=250)
    right_answer = models.CharField(max_length=250, null=False, default='right answer')
    wrong_answer = models.CharField(max_length=250, null=False, default='wrong answer')
    add_at = models.DateTimeField(auto_now=True)
    update_at = models.DateTimeField(auto_now=True)
    question_type = models.CharField(max_length=50, default='Base')
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.name


class QuizLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    create_at = models.DateTimeField(default=timezone.now)
    update_at = models.DateTimeField(auto_now=True)
    finish_period = models.FloatField(null=True)
    score = models.IntegerField(null=True, default=0)

    def __str__(self):
        return User.objects.get(pk=self.user).user_name + "got " + self.score + "at" + self.update_at


class QuizDetail(models.Model):
    quizLog = models.ForeignKey(QuizLog, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    detail = models.CharField(max_length=250)
    create_at = models.DateTimeField(default=timezone.now)
    update_at = models.DateTimeField(auto_now=True)


class QuestionDetail(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quizLog = models.ForeignKey(QuizLog, blank=True, null=True, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    detail = models.CharField(max_length=250)
    create_at = models.DateTimeField(default=timezone.now)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return User.objects.get(pk=self.user).user_name + "got at" + self.create_at


class Type(models.Model):
    name = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE,  default=1)
    create_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name