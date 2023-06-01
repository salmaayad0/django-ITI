from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Courses

# Create your views here.
# coursesList page
def coursesList(req):
    courses = Courses.objects.all()
    return render(req, 'courses/coursesList.html', {'courses': courses})

# add course page
def addCourse(req):
    if(req.method == 'POST'):
        Courses.objects.create(courseName=req.POST['courseName'])
        return HttpResponseRedirect('/courses')
    return render(req, 'courses/addCourse.html')

# delete course page
def deleteCourse(req, id):
    Courses.objects.filter(courseId=id).delete()
    return HttpResponseRedirect('/courses')



