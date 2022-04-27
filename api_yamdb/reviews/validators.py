from django.forms import ValidationError
from django.utils import timezone


def year_validator(value):
    if 0 > value > timezone.now().year:
        raise ValidationError(
            ('%(value)s is not a correcrt year!'),
            params={'value': value},
        )
