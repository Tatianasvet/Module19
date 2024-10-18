from django.db import models


# Create your models here.
class Buyer(models.Model):
    name = models.CharField(max_length=50)
    balance = models.DecimalField(max_digits=8, decimal_places=2)
    age = models.PositiveIntegerField()


class Game(models.Model):
    title = models.CharField(max_length=200)
    cost = models.DecimalField(max_digits=7, decimal_places=2)
    size = models.DecimalField(max_digits=6, decimal_places=1)
    description = models.TextField()
    age_limited = models.BooleanField(default=False)
    buyer = models.ManyToManyField(Buyer, related_name='games')