# -*- coding: utf-8 -*-
"""User related admin configs."""
from django.contrib import admin

from ..models import User
from ._user_admin import UserAdmin

admin.site.register(
    User,
    UserAdmin,
)
