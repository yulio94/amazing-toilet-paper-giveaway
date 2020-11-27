"""Celery tasks"""

# Django
from django.conf import settings
from django.core.mail import send_mail

# Celery
from celery import shared_task


@shared_task
def send_email(subject, template, email):
    send_mail(
        subject,
        "",
        settings.DEFAULT_FROM_EMAIL,
        [email],
        html_message=template,
    )
    return True
