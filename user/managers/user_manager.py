# -*- coding: utf-8 -*-
from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    """A UserManager that doesn't require username."""
    def _create_user(
        self,
        email,
        password,
        **extra_fields,
    ):
        """
        Create and save a user with the given email, and password.
        As parent but without username.
        """
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email = email, **extra_fields)
        user.set_password(password)
        user.save(using = self._db)
        return user

    def create_user(
        self,
        email = None,
        password = None,
        **extra_fields,
    ):
        """
        Create and save a user with the given email, and password.
        Handle defaults for is_staff and is_superuser.
        As parent but without username.
        """
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(
        self,
        email = None,
        password = None,
        **extra_fields,
    ):
        """
        Create and save a user with the given email, and password.
        As parent but without username.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self._create_user(email, password, **extra_fields)
