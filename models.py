from django.db import models

# Create your models here.

class Message(models.Model):
    id = models.CharField(max_length=32, primary_key=True)
    messageString = models.TextField()
