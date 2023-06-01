from django.urls import path
from . import views

urlpatterns = [
    path('', views.coursesList, name='coursesList'),
    path('/addcourse', views.addCourse, name='addCourse'),
    path('/deletecourse/<int:id>', views.deleteCourse, name='deleteCourse')
]
