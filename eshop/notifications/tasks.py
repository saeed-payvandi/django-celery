from celery import shared_task
from celery import group, chain
import time

@shared_task(queue='tasks')
def send_sms_to_user():
    time.sleep(6)
    print('sms has been sent to user')

# @shared_task(queue='celery',rate_limit='1/m')
# def task_1():
#     time.sleep(3)
#     return
#
# @shared_task(queue='celery:1')
# def task_2():
#     time.sleep(3)
#     return
#
# @shared_task(queue='celery:2')
# def task_3():
#     time.sleep(3)
#     return
#
# @shared_task(queue='celery:3')
# def task_4():
#     time.sleep(3)
#     return

# group_tasks = group(task_1.s(), task_2.s(), task_3.s(), task_4.s())
# group_tasks.apply_async()

# chain_tasks = chain(task_1.s(), task_2.s(), task_3.s(), task_4.s())
# chain_tasks.apply_async()
