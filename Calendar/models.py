from django.db import models

# Create your models here.

class Calendar(models.Model):
    year = models.IntegerField()
    month = models.IntegerField()
    day = models.IntegerField()