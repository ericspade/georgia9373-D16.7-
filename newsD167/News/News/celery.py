import os
from celery import Celery
from django.conf import settings
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'News.settings')

app = Celery('news', broker='redis://localhost')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.conf.beat_schedule = {
    'weekly send-out': {
        'task': 'newsapp.tasks.weekly_news',
        'schedule': crontab(),
    },
}

app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
