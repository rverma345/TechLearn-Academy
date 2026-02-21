from django.shortcuts import render
from .models import Course, Trainer, Student


def home(request):
    context = {
        'total_courses': Course.objects.count(),
        'total_trainers': Trainer.objects.count(),
        'total_students': Student.objects.count(),
    }
    return render(request, 'home.html', context)


def course_list(request):
    courses = Course.objects.all()
    return render(request, 'courses.html', {'courses': courses})


def trainer_list(request):
    trainers = Trainer.objects.all()
    return render(request, 'trainers.html', {'trainers': trainers})


def student_list(request):
    students = Student.objects.all()
    return render(request, 'students.html', {'students': students})