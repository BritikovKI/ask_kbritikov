from __future__ import unicode_literals
from datetime import datetime
from django.db import models

# class Question(models.Model):
class User(models.model):
    nickname=models.CharField(max_length=10)
    email=models.EmailField()
    img=models.CharField(max_length=10)

class Tag(models.Model):
    tagtext=models.CharField(max_length=10)
    correct=models.BooleanField()

class Post(models.Model):
    user=models.ForeignKey(User)
    text=models.TextField()
    tags=models.ManyToManyField()

class Answer(models.Model):
    post=models.ForeignKey(Post)
    text=models.TextField()
    user=models.ForeignKey()