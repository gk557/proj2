from dataclasses import fields
from pyexpat import model
from django import forms
from student_portal.models import student

class StudentForm(forms.ModelForm):
    class Meta:
        model=student
        fields="__all__"