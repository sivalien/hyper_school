from django.urls import path

from .views import MainView, CourseView, TeacherView, AddCourseView, student_signup_view, StudentLoginView


urlpatterns = [
    path('schedule/main/', MainView.as_view(), name='main'),
    path('schedule/course_details/<int:course_id>', CourseView.as_view(), name='course'),
    path('schedule/teacher_details/<int:teacher_id>', TeacherView.as_view(), name='teacher'),
    path('schedule/add_course/', AddCourseView.as_view(), name='add_course'),
    path('signup/', student_signup_view, name="student_signup"),
    path('login/', StudentLoginView.as_view(), name="student_login"),
]