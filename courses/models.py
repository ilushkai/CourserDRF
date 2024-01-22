from django.db import models

from config import settings

NULLABLE = {'null': True, 'blank': True}


class Course(models.Model):
    title = models.CharField(max_length=35, verbose_name='Название')
    description = models.TextField(verbose_name='Описание', **NULLABLE)
    preview = models.ImageField(upload_to='courses/', **NULLABLE, verbose_name='превью')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Создатель курса',
                              related_name='ownerCourse', **NULLABLE)
    price = models.IntegerField(verbose_name='Цена', **NULLABLE)

    def __str__(self):
        return f'Название: {self.title} ({self.description})'

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'


class Lesson(models.Model):
    title = models.CharField(max_length=35, verbose_name='Название')
    description = models.TextField(verbose_name='Описание', **NULLABLE)
    preview = models.ImageField(upload_to='courses/', **NULLABLE, verbose_name='превью')
    link = models.URLField(max_length=200, **NULLABLE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Курс', related_name='course')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Создатель урока',
                              related_name='ownerLesson', **NULLABLE)

    def __str__(self):
        return f'Название: {self.title} ({self.description})({self.link})'

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'



class Subscription(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True, blank=True)
    is_active = models.BooleanField(default=True, verbose_name='подписка')

    def __str__(self):
        return f'{self.is_active}'

    class Meta:
        verbose_name = 'подписка'
        verbose_name_plural = 'подписки'
