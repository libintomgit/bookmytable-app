from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=200)
    roll = models.CharField(max_length=50)
    is_classrep = models.BooleanField("Classrep", default=False)