from dataclasses import fields
from pyexpat import model
from django import forms
from app1.models import student

class StudentForm(forms.ModelForm):
    class Meta:
        model=student
        fields="__all__"

