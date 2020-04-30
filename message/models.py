from django.db import models
from datetime import datetime

# Create your models here.
class Message(models.Model):
    userlogid = models.AutoField(primary_key=True)
    fullname = models.CharField(max_length=150)
    topic = models.CharField(max_length=150)
    time = models.DateTimeField(default=datetime.now)
class Topic(models.Model):
    topic = models.CharField(max_length=150)
    name = models.CharField(max_length=150)
