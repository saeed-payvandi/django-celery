from celery import shared_task
from config.celery_config import app
import time


@app.task(queue='tasks', time_limit=5)
def send_mail_to_user():
    time.sleep(6)
    return "(* Email has been set to user successfully *)"


# @shared_task(queue='tasks')
# def send_mail_to_user():
#     # print('email has been send to user')
#     raise ConnectionError('connection lost...')
