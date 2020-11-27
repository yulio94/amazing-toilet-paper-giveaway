"""Business logic and use cases"""

# Python
import random

# Django
from django.template.loader import render_to_string
from django.urls import reverse_lazy

# Models
from apps.users.models import User

# Tasks
from apps.users.tasks import send_email

# utils
from apps.users.utils import gen_token, decode_token

# Exceptions
from jwt.exceptions import DecodeError


class EmailAlreadyExists(Exception):
    """Email already exists in database"""


class EmailIsNotValidException(Exception):
    """Email already exists in database"""


class TokenNotValidException(Exception):
    """token is not valid"""


class CreateNewUser:
    """Validate if user exists and create new"""

    def __init__(self, username, first_name, last_name, email):
        self._username = username
        self._first_name = first_name
        self._last_name = last_name
        self._email = email

    def execute(self):
        """"""
        self.valid_email()
        self._create_new_user()
        self._send_user_confirmation()

    def valid_email(self):
        """"""
        if User.objects.validate_email(self._email):
            raise EmailAlreadyExists

    def _create_new_user(self):
        """"""
        return User.objects.create_new_user(username=self._username, first_name=self._first_name,
                                            last_name=self._last_name, email=self._email)

    def _send_user_confirmation(self):
        """"""
        token = gen_token(self._email)

        url = reverse_lazy('change-password', kwargs={'token': token.decode('utf-8')})

        subject = 'Verificacion de cuenta'
        msg_html = render_to_string(
            'emails/user-confirmation.html',
            {'url': f'http://localhost:8000{url}'})
        send_email(subject, msg_html, self._email)


class ChangePasswordUser:
    """Validate and change user password"""

    def __init__(self, token, password):
        self._token = token
        self._password = password
        self._email = None

    def execute(self):
        """"""

        self.validate_data()
        self._change_user_password()

    def validate_data(self):
        try:
            self._email = decode_token(self._token.encode('utf-8'))
        except DecodeError as err:
            raise TokenNotValidException(err)

        try:
            User.objects.validate_email(self._email)
        except Exception as err:
            raise EmailIsNotValidException(err)

    def _change_user_password(self):
        return User.objects.change_password(email=self._email, password=self._password)


class RaffleResult:

    @staticmethod
    def make_raffle():
        """Create list of all ids in the user model and choice one"""
        ids = [obj.pk for obj in User.objects.all()]
        random_index = random.choice(ids)
        return User.objects.get(id=random_index)
