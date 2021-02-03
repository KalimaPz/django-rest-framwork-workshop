from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])


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
class RegisteredSubject(models.Model) :
    subject_id = models.CharField(max_length = 50)
    subject_name = models.CharField(max_length = 50)
    def __unicode__(self):
        return self.name

class Student(models.Model):
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    registed_subject = models.ForeignKey("RegisteredSubject", verbose_name=("Registed Subject"), on_delete=models.CASCADE)

class Snippet(models.Model) :
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length = 50 , blank=True, default = '')
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    language = models.CharField(choices = LANGUAGE_CHOICES, default = 'python', max_length = 100)
    style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)
    class Meta : 
        ordering = ['created']
    