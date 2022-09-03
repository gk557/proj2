from django.shortcuts import render, redirect
from django.http import HttpResponse
from student_portal.models import student
from student_portal.forms import StudentForm

# Create your views here.
def student_portal(request):
    if request.method == 'GET':
        form = StudentForm()
        students = student.objects.all()
        print(students)
        students_data = []
        for std in students:
            student_data = {}
            student_data['name'] = std.sname
            student_data['email'] = std.email
            student_data['jdate'] = std.jdate
            student_data['phnumber'] = std.phnumber
            students_data.append(student_data)
        return render(request, 'student_portal/student.html', {'students': students_data, 'form': form})
    if request.method == 'POST':
        print(request.POST)
        form=StudentForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            return HttpResponse("Not a valid form")
        return redirect('/student_portal')