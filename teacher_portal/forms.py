from django import forms

from dataclasses import fields
from pyexpat import model
from django import forms
from teacher_portal.models import teacher

class Teacherform(forms.ModelForm):
    class Meta:
        model=teacher
        fields="__all__"
        
