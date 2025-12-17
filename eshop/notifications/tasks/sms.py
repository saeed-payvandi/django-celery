from celery import shared_task
from config.celery_config import app
from celery import group
import time

phone_number = [
    '0912123456789',
    '0912123457888',
    '0903125432123',
    '0902345643212',
]


@app.task(queue='tasks')
def send_sms_to_user(phone_number: str):
    if phone_number.startswith("0903"):
        raise ValueError("invalid phone number")
    
    return f"Message has been sent to {phone_number}"


def handle_result(result):
    if result.successful():
        print(f'Task completed: {result.get()}')
    elif result.failed() and isinstance(result.result, ValueError):
        print(f'Task faild: {result.result}')
    elif result.status == 'REVOKED':
        print(f'Task was revoked: {result.id}')


def run_tasks():
    task_group = group(send_sms_to_user.s(number) for number in phone_number)
    result_group = task_group.apply_async()
    result_group.get(disable_sync_subtasks=False, propagate=False)

    for result in result_group:
        handle_result(result)


# @app.task(queue='tasks', autoretry_for=(ConnectionError,), default_retry_delay=5, retry_kwargs={'max_retries': 5})
# def send_sms_to_user():
#     raise ConnectionError('sms connection error....')


# @shared_task(queue='tasks')
# def send_sms_to_user():
#     print('sms has been sent to user')
