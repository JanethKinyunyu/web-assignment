from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Student, Teacher

class StudentRegistrationForm(UserCreationForm):
    class Meta:
        model = Student
        fields = ['username','firt_name', 'middle_name', 'last_name', 'enrolled_course', 'password1', 'password2']

class StudentAuthenticationForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class TeacherRegistrationForm(UserCreationForm):
    class Meta:
        model = Teacher
        fields = ['username', 'password1', 'password2']

class TeacherAuthenticationForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)