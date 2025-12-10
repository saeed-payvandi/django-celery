import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
app = Celery('config')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.task_routes={
    'notifications.tasks.send_discount_emails': {'queue': 'queue1'},
    'notifications.tasks.process_data_for_ml': {'queue': 'queue2'},
}

app.autodiscover_tasks()
