from django.db import models

# Create your models here.
class Courses(models.Model):
    courseId = models.AutoField(primary_key=True)
    courseName = models.CharField(max_length=50)
    
    def __str__(self):
        return self.courseName
    
    
