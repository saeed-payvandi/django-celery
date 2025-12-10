from celery import Celery

app = Celery('tasks')
app.config_from_object('celery_config')

app.conf.imports = ('notifications.tasks',)
app.autodiscover_tasks()