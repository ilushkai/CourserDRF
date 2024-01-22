from django.contrib import admin
from courses.models import *
from pay.models import Payments


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'preview', 'link', 'course',)


