from django.urls import path
from .views import *


urlpatterns = [
    #USER URLS
    path('list-user/', UserViewAPI.as_view()),
    path('create-user/', UserCreateAPI.as_view()),
    path('update-user/<int:pk>/', UserUpdateAPI.as_view()),
    path('delete-user/<int:pk>/', UserDeleteAPI.as_view()),

    #STUDENT URLS
    path('create-student/', StudentCreateAPI.as_view()),
    path('list-student/', StudentViewAPI.as_view()),
    path('update-student/<int:pk>/', StudentUpdateAPI.as_view()),
    path('delete-student/<int:pk>/', StudentDeleteAPI.as_view()),

    #COURSE URLS
    path('create-course/', CourseCreateAPI.as_view()),
    path('list-course/', CourseViewAPI.as_view()),
    path('update-course/<int:pk>/', CourseUpdateAPI.as_view()),
    path('delete-course/<int:pk>/', CourseDeleteAPI.as_view()),

    #GRADE URLS
    path('create-grade/', GradeCreateAPI.as_view()),
    path('list-grade/', GradeViewAPI.as_view()),
    path('update-grade/<int:pk>/', GradeUpdateAPI.as_view()),
    path('delete-grade/<int:pk>/', GradeDeleteAPI.as_view()),

    #TEACHER URLS
    path('create-teacher/', TeacherCreateAPI.as_view()),
    path('list-teacher/', TeacherViewAPI.as_view()),
    path('update-teacher/<int:pk>/', TeacherUpdateAPI.as_view()),
    path('delete-teacher/<int:pk>/', TeacherDeleteAPI.as_view()),
]
