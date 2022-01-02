# -*- coding: utf-8 -*-
from typing import Optional

from django.core.exceptions import ValidationError
from django.utils.functional import Promise
from django.utils.translation import gettext_lazy as _

from ..models import User


class EachCaseValidator:
    """Validates upper and lowercase characters are present in a password."""

    def __init__(
        self,
        min_uppercase: Optional[int] = 1,
        min_lowercase: Optional[int] = 1,
    ):
        """Sets up the number of upper and lowercase characters to require.

        Args:
            min_uppercase (Optional[int], optional): Minimum number of
                uppercase characters to require. Defaults to 1.
            min_lowercase (Optional[int], optional): Minimum number of
                lowercase characters to require. Defaults to 1.
        """
        self._min_uppercase = min_uppercase
        self._min_lowercase = min_lowercase

    @property
    def _message(self) -> type[Promise]:
        """Validation message.

        Returns:
            django.utils.functional.Promise: Lazy translated validation message.
        """
        return _(
            "This password must contain at least %(number_upper)d"
            " uppercase and %(number_lower)d lowercase characters.",
        )

    @property
    def _message_params(self) -> dict[str:int]:
        """Validation message parameters.

        Returns:
            dict[str: int]: A dictionary of validation message formatting values.
        """
        return {
            "number_upper": self._min_uppercase,
            "number_lower": self._min_lowercase,
        }

    def validate(
        self,
        password: str,
        user: Optional[type[User]] = None,
    ) -> None:
        """Validates the password.

        Args:
            password (str): Password to be validated.
            user (user.models.User, optional): User trying
                to set the password. Defaults to None.

        Raises:
            ValidationError: If not enough uppercase or
                lowercase characters are in the password.
        """
        if (
            len([c for c in password if c.isupper()]) < self._min_uppercase
            or len([c for c in password if c.islower()]) < self._min_lowercase
        ):
            raise ValidationError(
                self._message,
                code="password_case_not_varied",
                params=self._message_params,
            )

    def get_help_text(self) -> str:
        """Returns help text.

        Returns:
            str: Help text.
        """
        return self._message % self._message_params
