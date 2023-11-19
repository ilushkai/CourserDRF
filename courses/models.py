from django.db import models

from users.models import NULLABLE


class Course(models.Model):
    title = models.CharField(max_length=35, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    preview = models.ImageField(upload_to='courses/', **NULLABLE, verbose_name='превью')

    def __str__(self):
        return f'Название: {self.title} ({self.description})'

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'



class Lesson(models.Model):
    title = models.CharField(max_length=35, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    preview = models.ImageField(upload_to='courses/', **NULLABLE, verbose_name='превью')
    link = models.URLField(max_length=200, **NULLABLE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Курс')

    def __str__(self):
        return f'Название: {self.title} ({self.description})({self.link})'

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'
