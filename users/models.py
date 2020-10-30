from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
class CustomUserEntity(AbstractUser):
    email = models.EmailField(_('email address'), unique=True)
    username = None
    is_staff = None
    is_superuser = None
    date_joined = None
    is_active = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []