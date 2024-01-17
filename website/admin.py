from django.contrib import admin
from .models import State,College,Course,Scheme,Student

# Register your models here.

admin.site.register(State)
admin.site.register(College)
admin.site.register(Course)
admin.site.register(Scheme)
admin.site.register(Student)

