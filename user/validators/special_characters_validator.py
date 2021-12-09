from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _


class SpecialCharactersValidator():
    """Validate special characters are present in a password."""
    def __init__(self, min_special = 1):
        """Set up the number of special characters to require."""
        self._min_special = min_special

    @property
    def _special_characters(self):
        """Return the special characters."""
        return [c for c in ';<=>?@[\\]^_`{|}~¡¢£¤¥¦§¨©«¬®¯°±´¶·¸»¼½¾¿×÷']

    @property
    def _message(self):
        """Return the validation message."""
        return _(
            'This password must contain at least %(number_required)d'
            ' special characters. i.e %(special_characters)s',
        )

    @property
    def _message_params(self):
        """Return the validation message parameters."""
        return {
            'number_required': self._min_special,
            'special_characters': ''.join(self._special_characters),
        }

    def validate(self, password, user = None):
        """Validate the password."""
        if len([c for c in password if c in self._special_characters]
               ) < self._min_special:
            raise ValidationError(
                self._message,
                code = 'password_not_enough_specials',
                params = self._message_params,
            )

    def get_help_text(self):
        """Return the help text."""
        return self._message % self._message_params
