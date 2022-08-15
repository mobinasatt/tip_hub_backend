# Django packages
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
# Local apps
from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(verbose_name='Email address', max_length=255,
                            unique=True)
    phone_number = models.CharField(max_length=11, unique=True)
    fullname = models.CharField(max_length=255)
    bio = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='user/images/', null=True, blank=True)
    age = models.IntegerField(default=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['email', 'fullname']

    def __str__(self):
        return self.phone_number

    @property
    def is_staff(self):
        return self.is_admin
