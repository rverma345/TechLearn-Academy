from django.db import models

# Create your models here.
class Course(models.Model):
    course_name=models.CharField(max_length=50)
    description=models.CharField(max_length=50)
    duration=models.IntegerField(help_text='Duration in Weeks')
    course_image=models.ImageField(upload_to="courses/", blank=True,null=True)

    def __str__(self):
        return self.course_name

class Trainer(models.Model):
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    email=models.EmailField(unique=True)
    expertise=models.CharField(max_length=100)
    trainer_photo= models.ImageField(upload_to='trainers/',blank=True,null=True)

    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    def __str__(self):
        return self.full_name()


class Student(models.Model):
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    email=models.EmailField(unique=True)
    is_active=models.BooleanField(default=True)
    enrolled_course=models.ForeignKey(Course,on_delete=models.CASCADE)
    trainer=models.ForeignKey(Trainer,on_delete=models.SET_NULL,null=True)

    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
