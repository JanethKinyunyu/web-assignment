from django.contrib.auth.models import User
from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=255, blank=True, null=True)
    Middle_name = models.CharField(max_length=255,blank=True, null=True)
    Last_name = models.CharField(max_length=255, blank=True, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    student_id = models.CharField(max_length=10, unique=True, editable=False)
    
    def __str__(self):
        return f'{self.user.username} ({self.student_id})'

class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class Course(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10, unique=True)
    modules = models.ManyToManyField('Module')

    def __str__(self):
        return f'{self.name} ({self.code})'

class Module(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Result(models.Model):
    RESULT_CHOICES = [
        ('Pass', 'Pass'),
        ('Supplementary', 'Supplementary'),
        ('Disqualified', 'Disqualified'),
    ]

    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    module = models.ForeignKey(Module, on_delete=models.CASCADE)
    score = models.DecimalField(max_digits=5, decimal_places=2)
    result_type = models.CharField(max_length=15, choices=RESULT_CHOICES)

    def __str__(self):
        return f'{self.student} - {self.course} - {self.module} - {self.result_type}'