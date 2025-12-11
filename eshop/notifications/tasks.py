from celery import shared_task
import time

@shared_task
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
