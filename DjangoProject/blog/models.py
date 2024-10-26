from django.db import models

# Create your models here.


class Message(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

