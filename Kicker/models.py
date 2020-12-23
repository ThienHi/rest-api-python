from django.db import models
from datetime import date

# Create your models here.


class Kicker(models.Model):
    name = models.CharField(max_length=50)
    dateOfBirth = models.DateField()
    height = models.FloatField()
    number = models.IntegerField()
    image = models.CharField(max_length=500)
