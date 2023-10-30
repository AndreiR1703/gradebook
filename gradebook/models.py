from django.core.validators import MaxValueValidator
from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password



# Create your models here.


class Grade(models.Model):
    student_name = models.CharField(max_length=100, blank=True)
    course_name = models.CharField(max_length=100)
    course_grade = models.PositiveIntegerField(validators=[MaxValueValidator(10, message="Grade must be less than or equal to 10.")])
    date_added = models.DateTimeField(default=datetime.now, blank=True)
    # added_by = models.CharField(default=User.objects.get(), max_length=100)
    added_by = models.CharField(default="prof1", max_length=100)

    def __str__(self):
        return self.course_name

class Utilizator(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #aici am legat modelul meu de modelul User din django
    username = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    is_teacher = models.BooleanField()
    USERNAME_FIELD = 'username'
    
    # def save(self, *args, **kwargs):
    #     self.password = make_password(self.password)
    #     super().save(*args, **kwargs)