from django.db import models
from django.contrib.auth.models import User

# Create your models here.
    
class Course(models.Model):
    course_code = models.CharField(max_length=100, primary_key=True)
    semester_course = models.BooleanField(default=False)
    online = models.BooleanField(default=False)
    active = models.BooleanField(default=False)
    
    def __str__(self):
        return self.course_code
    
class Student(models.Model):
    sid = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    major = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    
    def __str__(self):
        return self.sid.last_name
    
class Tutor(models.Model):
    tid = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    course_code =  models.ForeignKey(Course, on_delete=models.CASCADE)
    pay = models.IntegerField()
    availability = models.CharField(max_length=100)
    def __str__(self):
        return self.tid.last_name
    
class Assignment(models.Model):
    tutor = models.ForeignKey(Tutor, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, null=True)
    date = models.DateField(null= True, blank=False)
    
    class Meta:
        unique_together = ('tutor', 'student', 'date')