from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework import generics
from .permissions import IsTeacher


#USER CRUD
class UserCreateAPI(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # permission_classes = (IsTeacher, )


class UserViewAPI(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserUpdateAPI(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDeleteAPI(generics.RetrieveDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


#STUDENT CRUD
class StudentCreateAPI(generics.CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentViewAPI(generics.ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentUpdateAPI(generics.UpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentDeleteAPI(generics.RetrieveDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


#COURSE CRUD
class CourseCreateAPI(generics.CreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CourseViewAPI(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CourseUpdateAPI(generics.UpdateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CourseDeleteAPI(generics.RetrieveDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


#TEACHER CRUD
class TeacherCreateAPI(generics.CreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


class TeacherViewAPI(generics.ListAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer



class TeacherUpdateAPI(generics.UpdateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


class TeacherDeleteAPI(generics.RetrieveDestroyAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


#GRADE CRUD
class GradeCreateAPI(generics.CreateAPIView):
    queryset = Grade.objects.all()
    serializer_class = GradeSerializer


class GradeViewAPI(generics.ListAPIView):
    queryset = Grade.objects.all()
    serializer_class = GradeSerializer


class GradeUpdateAPI(generics.UpdateAPIView):
    queryset = Grade.objects.all()
    serializer_class = GradeSerializer


class GradeDeleteAPI(generics.RetrieveDestroyAPIView):
    queryset = Grade.objects.all()
    serializer_class = GradeSerializer