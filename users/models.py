from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_('Email address'), unique=True)
    avatar = ProcessedImageField(
        upload_to='avatars',
        processors=[ResizeToFill(500, 500)],
        format='JPEG',
        options={'quality': 60}, blank=True
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email