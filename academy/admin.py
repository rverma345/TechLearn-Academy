from django.contrib import admin
from .models import Course,Trainer,Student
# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    list_display= ['course_name','duration']
    search_fields=['course_name']
    list_filter=['course_name']


class TrainerAdmin(admin.ModelAdmin):
    list_display=['full_name','email','expertise',]
    search_fields=['full_name','expertise']
    list_filter=['first_name','last_name']


class StudentAdmin(admin.ModelAdmin):
    list_display=['full_name','email','enrolled_course','trainer','is_active']
    search_fields=['full_name','enrolled_course','trainer']
    list_filter=['is_active','enrolled_course']



admin.site.register(Course,CourseAdmin)
admin.site.register(Trainer,TrainerAdmin)
admin.site.register(Student,StudentAdmin)