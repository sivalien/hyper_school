from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm

from .models import Course, Teacher
from .forms import StudentSignUpForm


class MainView(View):
    def get(self, request, *args, **kwargs):
        query = self.request.GET.get("q")
        if query is None:
            courses = Course.objects.all()
        else:
            courses = Course.objects.filter(title__contains=query)
        return render(request, 'schedule/search.html', {'courses': courses, 'count': courses.count()})


class CourseView(View):
    def get(self, request, *args, **kwargs):
        id = kwargs['course_id']
        course = Course.objects.get(pk=id)
        return render(request, 'schedule/course.html', {"course": course})


class TeacherView(View):
    def get(self, request, *args, **kwargs):
        id = kwargs['teacher_id']
        teacher = Teacher.objects.get(pk=id)
        return render(request, 'schedule/teacher.html', {"teacher": teacher})


class AddCourseView(View):
    def get(self, request, *args, **kwargs):
        form = StudentSignUpForm()
        return render(request, 'schedule/add_course.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = StudentSignUpForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('add_course')


def student_signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # user = form.save()
            # login(request, user)
            return redirect('/schedule/main/')
        else:  # submitted registration data is invalid
            pass  # maybe add some extra error messages
    else:  # request method is not POST
        form = UserCreationForm()
    context = {'form': form}
    return render(request, 'schedule/signup.html', context)


class StudentLoginView(LoginView):
    template_name = 'schedule/login.html'
    next_page = '/schedule/main/'
