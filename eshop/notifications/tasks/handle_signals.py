from config.celery_config import app
from celery.signals import task_failure
import sys


@app.task(queue='tasks')
def my_task():
    raise ValueError("Task Failed")


@app.task(queue='tasks')
def error_handler_task(task_id):
    sys.stdout.write(f'Task id is {task_id}.')


@task_failure.connect(sender=my_task)
def handle_my_task_failure(sender=None, task_id=None, **kwargs):
    error_handler_task.delay(task_id)


def run_task():
    my_task.delay()
