# Django
from django.conf import settings
from django.utils import timezone

# Utilities
import jwt
from datetime import timedelta


def gen_token(email):
    """Generate jwt """
    exp_date = timezone.now() + timedelta(days=3)
    payload = {
        'email': email,
        'exp': int(exp_date.timestamp()),
        'type': 'email_confirmation'
    }
    return jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')


def decode_token(token):
    """Decode token"""
    try:
        token = jwt.decode(token, settings.SECRET_KEY, algorithms='HS256')
    except Exception as err:
        raise Exception(err)
    return token['email']
