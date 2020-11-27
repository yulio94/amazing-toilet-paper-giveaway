"""Extends model functionality"""

# Models
from django.db import models


class UserManager(models.Manager):
    """Managers to manage users queries"""

    def create_new_user(self, **kwargs):
        return self.get_queryset().create(**kwargs)

    def change_password(self, email, password):
        user = self.get_queryset().get(email=email)
        user.set_password(password)
        user.is_active = True
        user.save()

    def validate_email(self, email):
        return self.get_queryset().filter(email=email).exists()
