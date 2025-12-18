from config.celery_config import app
from datetime import timedelta

app.conf.beat_schedule = {
    'task_1': {
        'task': 'notifications.tasks.schedule_tasks.task_1',
        'schedule': timedelta(seconds=5)
    },
    'task_2': {
        'task': 'notifications.tasks.schedule_tasks.task_2',
        'schedule': timedelta(seconds=10)
    },
}


@app.task(queue='tasks')
def task_1():
    print('Running task 1')


@app.task(queue='tasks')
def task_2():
    print('Running task 2')