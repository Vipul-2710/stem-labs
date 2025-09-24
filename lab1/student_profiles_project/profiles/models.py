from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()                   # Student's age
    course = models.CharField(max_length=100)     # Course enrolled
    email = models.EmailField()                   # Contact email
    def __str__(self):
        return self.name
