from django.core.exceptions import ValidationError
from django.core.validators import validate_email

def validate_email_address(email):
    try:
        validate_email(email)
    except ValidationError:
        return {'error': 'Invalid email address'}
    return {}
