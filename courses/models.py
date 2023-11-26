from django.db import models

from config import settings

NULLABLE = {'null': True, 'blank': True}


class Course(models.Model):
    title = models.CharField(max_length=35, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    preview = models.ImageField(upload_to='courses/', **NULLABLE, verbose_name='превью')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Создатель курса',
                              related_name='ownerCourse', **NULLABLE)

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
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Курс', related_name='course')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Создатель урока',
                              related_name='ownerLesson', **NULLABLE)

    def __str__(self):
        return f'Название: {self.title} ({self.description})({self.link})'

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'


class PaymentType(models.Model):
    name = models.CharField(null=True, max_length=25)
    description = models.CharField(null=True, max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Способ оплаты"
        verbose_name_plural = "Способы оплаты"


class Payments(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, verbose_name='Пользователь',
                             related_name='user')
    date_of_payment = models.DateField(auto_now_add=True, verbose_name='Дата покупки')
    paid_course = models.ForeignKey(Course, on_delete=models.PROTECT, verbose_name='оплаченный курс',
                                    related_name='paid_course', **NULLABLE)
    paid_lesson = models.ForeignKey(Lesson, on_delete=models.PROTECT, verbose_name='оплаченный Урок',
                                    related_name='paid_lesson', **NULLABLE)
    payment_sum = models.IntegerField(verbose_name='Сумма оплаты')
    payment_method = models.ForeignKey(PaymentType, on_delete=models.PROTECT, **NULLABLE)

    def __str__(self):
        return f'Название: {self.user} - {self.paid_course}'

    class Meta:
        verbose_name = 'Платеж'
        verbose_name_plural = 'Платежи'
