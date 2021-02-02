from django.shortcuts import render
from .models import Person
from .serializers import PersonSerializer
from rest_framework import viewsets
# Create your views here.

class PersonViewset(viewsets.ModelViewSet):
    queryset = Person.objects.all().order_by('first_name')
    serializer_class = PersonSerializer

