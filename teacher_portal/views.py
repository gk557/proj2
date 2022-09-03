from lib2to3.pgen2.token import tok_name
from pickle import GET
from urllib import request
from django.shortcuts import render, redirect
from django.http import HttpResponse
from teacher_portal.models import teacher
from teacher_portal.forms import Teacherform

# Create your views here.

def teacher_portal(request):
    if request.method == 'GET':
        form = Teacherform()
        teachers = teacher.objects.all()
        print(teachers)
        teachers_data = []
        for tea in teachers:
            teacher_data = {}
            teacher_data['name'] = tea.tname
            teacher_data['branch'] = tea.branch
            teacher_data['email'] = tea.email
            teacher_data['jdate'] = tea.jdate
            teacher_data['phnumber'] = tea.phnumber
            teachers_data.append(teacher_data)
        return render(request, 'teacher_portal/teacher.html', {'teachers' : teachers_data, 'form' : form})
    if request.method == 'POST':
        print(request.POST)
        form=Teacherform(request.POST)
        if form.is_valid():
            form.save()
        else:
            return HttpResponse("Not a valid form")
        return redirect('/teacher_portal')
