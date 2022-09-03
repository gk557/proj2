from django.urls import path
from app1 import views
from proj2.app1.views import Student

urlpatterns=[
    path('',views.sample,name='sample'),
    path('/student', views.Student, name='student')
]