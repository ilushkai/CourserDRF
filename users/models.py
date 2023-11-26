from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

NULLABLE = {'null': True, 'blank': True}

class UserRoles(models.TextChoices):
    MEMBER = 'member', _('member'),
    MODERATOR = 'moderator', _('moderator'),



class User(AbstractUser):
    username = None

    email = models.EmailField(unique=True, verbose_name='Email')

    avatar = models.ImageField(upload_to='users/', verbose_name='аватар', **NULLABLE)
    phone = models.CharField(max_length=35, verbose_name='номер телефона', **NULLABLE)
    country = models.CharField(max_length=20, verbose_name='страна', **NULLABLE)

    role = models.CharField(max_length=10, choices=UserRoles.choices, default=UserRoles.MEMBER)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


