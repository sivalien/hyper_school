from django.db import models
from django.shortcuts import reverse


class Teacher(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    age = models.IntegerField()
    about = models.TextField()


class Course(models.Model):
    title = models.CharField(max_length=100)
    info = models.TextField()
    duration_months = models.IntegerField()
    price = models.IntegerField()
    teacher = models.ManyToManyField(Teacher)

    def get_absolute_url(self):
        return reverse('/schedule/course_details', kwargs={'id': self.id})


class Student(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    age = models.IntegerField()
    course = models.ManyToManyField(Course)
