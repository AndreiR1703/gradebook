from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


# Create your models here.


class Grade(models.Model):
    student_name = models.CharField(max_length=100, blank=True)
    course_name = models.CharField(max_length=100)
    course_grade = models.PositiveIntegerField()
    date_added = models.DateTimeField(default=datetime.now, blank=True)
    # added_by = models.CharField(default=User.objects.get(), max_length=100)
    added_by = models.CharField(default="prof1", max_length=100)

    def __str__(self):
        return self.course_name
