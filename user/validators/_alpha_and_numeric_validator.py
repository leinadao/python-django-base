# -*- coding: utf-8 -*-
from typing import Optional

from django.core.exceptions import ValidationError
from django.utils.functional import Promise
from django.utils.translation import gettext_lazy as _

from ..models import User


class AlphaAndNumericValidator:
    """Validates alpha and numeric characters are present in a password."""

    def __init__(
        self,
        min_alpha: Optional[int] = 1,
        min_numeric: Optional[int] = 1,
    ) -> None:
        """Sets up the number of alpha and numeric characters to require.

        Args:
            min_alpha (int, optional): Minimum number of
                alpha characters to require. Defaults to 1.
            min_numeric (int, optional): Minimum number of
                numeric characters to require. Defaults to 1.
        """
        self._min_alpha = min_alpha
        self._min_numeric = min_numeric

    @property
    def _message(self) -> type[Promise]:
        """Validation message.

        Returns:
            django.utils.functional.Promise: Lazy translated validation message.
        """
        return _(
            "This password must contain at least %(number_alpha)d"
            " alpha and %(number_numeric)d numeric characters.",
        )

    @property
    def _message_params(self) -> dict[str:int]:
        """Validation message parameters.

        Returns:
            dict[str: int]: A dictionary of validation message formatting values.
        """
        return {
            "number_alpha": self._min_alpha,
            "number_numeric": self._min_numeric,
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
            ValidationError: If not enough alpha or
                numeric characters are in the password.
        """
        if (
            len([c for c in password if c.isalpha()]) < self._min_alpha
            or len([c for c in password if c.isdigit()]) < self._min_numeric
        ):
            raise ValidationError(
                self._message,
                code="password_not_alphanumeric",
                params=self._message_params,
            )

    def get_help_text(self) -> str:
        """Returns help text.

        Returns:
            str: Help text.
        """
        return self._message % self._message_params
