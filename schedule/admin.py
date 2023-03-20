from django.contrib import admin

from .models import Teacher, Course, Student


class TeacherAdmin(admin.ModelAdmin):
    pass


class CourseAdmin(admin.ModelAdmin):
    pass


class StudentAdmin(admin.ModelAdmin):
    pass


admin.register(TeacherAdmin, Teacher)
admin.register(CourseAdmin, Course)
admin.register(StudentAdmin, Student)
