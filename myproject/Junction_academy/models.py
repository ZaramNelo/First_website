from django.db import models

# Create your models here.
class Account_owners(models.Model):
    Fullname = models.CharField(max_length=64)
    Email = models.CharField(max_length=64, unique=True)
    Number = models.IntegerField()
    password = models.CharField()

class Free_trials_list(models.Model):
    Fullname = models.CharField(max_length=64)
    Email = models.CharField(max_length=64, unique=True)
    Date = models.DateField()
    Time = models.TimeField()

