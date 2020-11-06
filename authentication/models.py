from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
from face_recognition_login import settings


class CustomUserEntity(AbstractUser):
    email = models.EmailField(_('email address'), unique=True)
    password = None
    username = None
    is_staff = None
    is_superuser = None
    date_joined = None
    is_active = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


class ImageEntity(models.Model):
    custom_user_entity = models.ForeignKey('CustomUserEntity',
                                           null=False,
                                           default=1,
                                           on_delete=models.CASCADE,
                                           )
    image = models.ImageField(upload_to='staticfiles/photo/')
