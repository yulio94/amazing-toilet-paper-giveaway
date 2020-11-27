# Python standard library
import os

# Django
from django.conf import settings

# Celery
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'toiletpaper.settings')

app = Celery('toiletpaper')

# Using a string here means the worker will not have to
# pickle the object when using Windows.
app.config_from_object('django.conf:settings',
                       namespace='CELERY')

app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
