from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Question(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()


class Answer(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # 기존 모델을 속성으로 연결 / 연결된 Question이 삭제되면 답변도 삭제
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()