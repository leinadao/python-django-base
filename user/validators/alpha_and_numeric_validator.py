# -*- coding: utf-8 -*-
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _


class AlphaAndNumericValidator():
    """Validate alpha and numeric characters are present in a password."""
    def __init__(self, min_alpha = 1, min_numeric = 1):
        """Set up the number of alpha and numeric characters to require."""
        self._min_alpha = min_alpha
        self._min_numeric = min_numeric

    @property
    def _message(self):
        """Return the validation message."""
        return _(
            'This password must contain at least %(number_alpha)d'
            ' alpha and %(number_numeric)d numeric characters.',
        )

    @property
    def _message_params(self):
        """Return the validation message parameters."""
        return {
            'number_alpha': self._min_alpha,
            'number_numeric': self._min_numeric,
        }

    def validate(self, password, user = None):
        """Validate the password."""
        if (
            len([c for c in password if c.isalpha()]) < self._min_alpha
            or len([c for c in password if c.isdigit()]) < self._min_numeric
        ):
            raise ValidationError(
                self._message,
                code = 'password_not_alphanumeric',
                params = self._message_params,
            )

    def get_help_text(self):
        """Return the help text."""
        return self._message % self._message_params
