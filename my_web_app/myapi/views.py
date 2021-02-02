from django.shortcuts import render
from .models import Person , Employee
from .serializers import PersonSerializer, EmployeeSerializer
from rest_framework import viewsets
# Create your views here.

class PersonViewset(viewsets.ModelViewSet):
    queryset = Person.objects.all().order_by('first_name')
    serializer_class = PersonSerializer

class EmployeeViewset(viewsets.ModelViewSet):
    queryset = Employee.objects.all().order_by('first_name')
    serializer_class = EmployeeSerializer