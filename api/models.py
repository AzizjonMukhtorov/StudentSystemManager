from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    is_teacher = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
    email = models.EmailField(verbose_name=("email"), max_length=254, null=True)
    def __str__(self):
        return self.username


class Teacher(models.Model):
    teacher_name = models.CharField(max_length=50)
    teacher_surname = models.CharField(max_length=50)
    teacher_fathersname = models.CharField(max_length=50, null=True)
    teacher_email = User.email
    teacher_address = models.CharField(max_length=250)
    teacher_phone = models.CharField(max_length=13)
    user = models.OneToOneField(User, verbose_name=("User"), on_delete=models.CASCADE)

    def __str__(self):
        return self.teacher_name


class Student(models.Model):
    student_name = models.CharField(max_length=50)
    student_surname = models.CharField(max_length=50)
    student_fathersname = models.CharField(max_length=50, null=True)
    student_email = User.email
    student_address = models.CharField(max_length=250)
    student_phone = models.CharField(max_length=13)
    user = models.OneToOneField(User, verbose_name=("User"), on_delete=models.CASCADE)

    def __str__(self):
        return self.student_name
    

class Course(models.Model):
    course_name = models.CharField(max_length=50)
    course_start_at = models.DateTimeField()
    course_teacher = models.ForeignKey(Teacher, related_name='teacher', on_delete=models.CASCADE)
    course_students = models.ForeignKey(Student,related_name='student', on_delete=models.CASCADE)

    def __str__(self):
        return self.course_name
    

class Grade(models.Model):
    grade_student= models.ForeignKey(Student, related_name='grades', on_delete=models.CASCADE)
    grade_course= models.ForeignKey(Course, on_delete=models.CASCADE)
    grade = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.grade_student} ({self.grade_course}): {self.grade}"