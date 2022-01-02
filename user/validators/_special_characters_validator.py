# -*- coding: utf-8 -*-
from typing import Optional

from django.core.exceptions import ValidationError
from django.utils.functional import Promise
from django.utils.translation import gettext_lazy as _

from ..models import User


class SpecialCharactersValidator:
    """Validate special characters are present in a password."""

    def __init__(self, min_special: Optional[int] = 1) -> None:
        """Sets up the number of special characters to require.

        Args:
            min_special (int, optional): Minimum number of
                special characters to require. Defaults to 1.
        """
        self._min_special = min_special

    @property
    def _special_characters(self) -> list[str]:
        """Allowed special characters.

        Returns:
            list[str]: The list of allowed special characters.
        """
        return [c for c in ";<=>?@[\\]^_`{|}~¡¢£¤¥¦§¨©«¬®¯°±´¶·¸»¼½¾¿×÷"]

    @property
    def _message(self) -> type[Promise]:
        """Validation message.

        Returns:
            django.utils.functional.Promise: Lazy translated validation message.
        """
        return _(
            "This password must contain at least %(number_required)d"
            " special characters. i.e %(special_characters)s",
        )

    @property
    def _message_params(self) -> dict[str:int]:
        """Validation message parameters.

        Returns:
            dict[str: int]: A dictionary of validation message formatting values.
        """
        return {
            "number_required": self._min_special,
            "special_characters": "".join(self._special_characters),
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
            ValidationError: If not enough special
                characters are in the password.
        """
        if (
            len([c for c in password if c in self._special_characters])
            < self._min_special
        ):
            raise ValidationError(
                self._message,
                code="password_not_enough_specials",
                params=self._message_params,
            )

    def get_help_text(self) -> str:
        """Returns help text.

        Returns:
            str: Help text.
        """
        return self._message % self._message_params
