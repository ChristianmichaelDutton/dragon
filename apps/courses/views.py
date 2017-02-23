from django.shortcuts import render,redirect
from .models import Courses


# Create your views here.
def index(request):
    catalog={
        "course_load":Courses.objects.all()
    }
    return render (request,'courses/index.html', catalog)

def courses(request):
    Courses.objects.create(course_name=request.POST['course_name'],course_description=request.POST['course_description'])
    return redirect('/')

def destroy(request, id):
    data = {
    'courseId': Courses.objects.get(id=id),
    "courses": Courses.objects.filter(id=id)
    }
    return render(request, 'courses/destroy.html', data)

def remove(request, id):
    data = {
    'courseId': Courses.objects.get(id=id),
    "courses": Courses.objects.filter(id=id).delete()
    }
    return redirect('/')
