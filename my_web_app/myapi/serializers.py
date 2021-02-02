from rest_framework import serializers
from .models import Person , Employee

class PersonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta :
        model = Person 
        fields = ['first_name','last_name','location']
class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta :
        model = Employee
        fields = ['first_name','last_name','age','salary']