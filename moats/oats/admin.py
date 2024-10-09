from django.contrib import admin
from .models import Course, Tutor, Student, Assignment

# Register your models here.

admin.site.register(Course)
admin.site.register(Tutor)
admin.site.register(Student)
admin.site.register(Assignment)
