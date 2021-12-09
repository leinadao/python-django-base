from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _


class EachCaseValidator():
    """Validate upper and lowercase characters are present in a password."""
    def __init__(self, min_uppercase = 1, min_lowercase = 1):
        """Set up the number of upper and lowercase characters to require."""
        self._min_uppercase = min_uppercase
        self._min_lowercase = min_lowercase

    @property
    def _message(self):
        """Return the validation message."""
        return _(
            'This password must contain at least %(number_upper)d'
            ' uppercase and %(number_lower)d lowercase characters.',
        )

    @property
    def _message_params(self):
        """Return the validation message parameters."""
        return {
            'number_upper': self._min_uppercase,
            'number_lower': self._min_lowercase,
        }

    def validate(self, password, user = None):
        """Validate the password."""
        if (
            len([c for c in password if c.isupper()]) < self._min_uppercase
            or len([c for c in password if c.islower()]) < self._min_lowercase
        ):
            raise ValidationError(
                self._message,
                code = 'password_case_not_varied',
                params = self._message_params,
            )

    def get_help_text(self):
        """Return the help text."""
        return self._message % self._message_params
