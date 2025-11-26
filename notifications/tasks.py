from celery import shared_task


@shared_task
def send_discount_emails():
    pass