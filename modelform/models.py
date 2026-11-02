from django.db import models

# Create your models here.
class Student_Data(models.Model):
    name=models.CharField()
    email=models.EmailField()
    age=models.IntegerField()



    def __str__(self):
     return self.name 