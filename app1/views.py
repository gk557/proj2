from django.shortcuts import render
from app1.forms import StudentForm, UserInfoForm

# Create your views here.

def Student(request):
    form=StudentForm()
    if request.method =='POST':
        form=StudentForm(request.POST)
        if form.is_valid():
            form.save
        else:
            print("Invalid Data")
        form=StudentForm()
    return render(request,'app1/index.html',{'form':form})

def sample(request):
    return render(request,'app1/index.html')
