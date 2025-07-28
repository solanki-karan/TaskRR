from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import Student

def index(request):
    students = Student.objects.all()
    return render(request, 'index.html', {'students': students})
