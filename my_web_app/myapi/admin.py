from django.contrib import admin
from .models import Person , Employee , Student , Snippet

admin.site.register(Person)
admin.site.register(Employee)
admin.site.register(Student)
admin.site.register(Snippet)