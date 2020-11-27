"""User models"""

# Django
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

# Managers
from .managers import UserManager


class User(AbstractUser):
    email = models.EmailField(_('email address'), unique=True, error_messages={
        'unique': _("A user with that email already exists."),
    }, )
    password = models.CharField(_('password'), max_length=128, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    objects = UserManager()

    REQUIRED_FIELDS = ['email', 'first_name', 'last_name']
