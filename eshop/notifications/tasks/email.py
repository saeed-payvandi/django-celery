from celery import shared_task

@shared_task(queue='tasks')
def send_mail_to_user():
    # print('email has been send to user')
    raise ConnectionError('connection lost...')
