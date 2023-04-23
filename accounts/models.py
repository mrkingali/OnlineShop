from django.contrib.auth.models import AbstractBaseUser, AbstractUser
from django.db import models

from .managers import UserManager


class User(AbstractBaseUser):
    email = models.EmailField(unique=True, max_length=255)

    phone_number = models.CharField(unique=True, max_length=11)

    full_name = models.CharField(max_length=128)

    is_active = models.BooleanField(default=True)

    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'phone_number'

    REQUIRED_FIELDS = ['email', 'full_name']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin


class OtpCode(models.Model):
    phone_number = models.CharField(max_length=11, unique=True)
    code = models.PositiveSmallIntegerField()
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.phone_number}-{self.code}-{self.created}'
