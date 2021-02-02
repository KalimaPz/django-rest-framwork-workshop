from django.db import models

# Create your models here.
class Person(models.Model):
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    location = models.CharField(max_length = 50)

    def __str__(self) :
        return self.first_name + ' ' + self.last_name 
class Employee(models.Model):
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    age = models.PositiveIntegerField()
    salary = models.PositiveIntegerField()
    def __str__(self):
        return self.first_name + ' ' + self.last_name 