from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse("this is a home page")

from . models import Student , Employee
from . serializers import EmployeeSerializer , StudentSerializer
from  rest_framework import viewsets


class Studentt(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer


class Employeee(viewsets.ModelViewSet):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer


def home(request):
    return render(request,'api/home.html')

def about(request):
    return render(request,'api/about.html')

def course(request):
    return render(request,'api/course.html')

def features(request):
    return render(request,'api/features.html')
