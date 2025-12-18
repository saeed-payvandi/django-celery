from celery import shared_task
from config.celery_config import app
import time


@app.task(queue='tasks', time_limit=5) # after time_limit if task doesn't finish, the task will destroy
def send_mail_to_user():
    time.sleep(6)
    return "(* Email has been set to user successfully *)"


def send_email():
    result = send_mail_to_user.delay()

    try:
        task_result = result.get(timeout=4) # with timeout we will have a timeout message but the task will continue
    except TimeoutError:
        print("Task timed out")
        # result.revoke(terminate=True)


# @shared_task(queue='tasks')
# def send_mail_to_user():
#     # print('email has been send to user')
#     raise ConnectionError('connection lost...')
