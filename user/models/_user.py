# -*- coding: utf-8 -*-
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from ..managers import UserManager


class User(AbstractUser):
    """User model."""

    username = None
    email = models.EmailField(
        _("email address"),
        unique=True,
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = [
        "first_name",
        "last_name",
    ]  # Must not include USERNAME_FIELD.

    objects = UserManager()
