from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=255)
    roll_no = models.CharField(max_length=10)
    CG = models.BooleanField(default=False)
    FDS = models.BooleanField(default=False)
    OOP = models.BooleanField(default=False)
