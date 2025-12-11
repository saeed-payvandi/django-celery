from celery import shared_task
from celery import group, chain
import time

@shared_task(rate_limit='1/m')
def task_1(queue='celery'):
    time.sleep(3)
    return

@shared_task
def task_2(queue='celery:1'):
    time.sleep(3)
    return

@shared_task
def task_3(queue='celery:2'):
    time.sleep(3)
    return

@shared_task
def task_4(queue='celery:3'):
    time.sleep(3)
    return

# group_tasks = group(task_1.s(), task_2.s(), task_3.s(), task_4.s())
# group_tasks.apply_async()

# chain_tasks = chain(task_1.s(), task_2.s(), task_3.s(), task_4.s())
# chain_tasks.apply_async()
