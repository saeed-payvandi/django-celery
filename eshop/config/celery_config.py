import os
import time
import logging
from celery import Celery, Task
from kombu import Exchange, Queue



class CustomTask(Task):
    def on_failure(self, exc, task_id, args, kwargs, einfo):
        if isinstance(exc, ConnectionError):
            logging.error("Connection Error")
        else:
            print(f"task id: {task_id} got error")


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
app = Celery('config')
app.Task = CustomTask
app.config_from_object('django.conf:settings', namespace='CELERY')

# app.conf.task_routes={
#     'notifications.tasks.send_discount_emails': {'queue': 'queue1'},
#     'notifications.tasks.process_data_for_ml': {'queue': 'queue2'},
# }

# app.conf.task_default_rate_limit = '1/m'

# queue=>celery,celery:1,celery:2,celery:3

# app.conf.broker_transport_options = {
#     'priority_steps': list(range(10)),
#     'sep': ':',
#     'queue_order_strategy': 'priority',
# }

app.conf.task_queues = [
    Queue('tasks', Exchange('tasks'), routing_key='tasks', queue_arguments={'x-max-priority': 10}),
    Queue('dead_letter', routing_key='dead_letter'),
]

app.conf.task_acks_late = True
app.conf.task_default_priority = 5
app.conf.worker_prefetch_multiplier = 1
app.conf.worker_concurrency = 1

# base_dir = os.getcwd()
# task_folder = os.path.join(base_dir, 'notifications', 'app_tasks')

# if os.path.exists(task_folder) and os.path.isdir(task_folder):
#     task_module = []
#     for filename in os.listdir(task_folder):
#         if filename.startswith("tasks_") and filename.endswith(".py"):
#             module_name = f"notifications.app_tasks.{filename[:-3]}"
#             module = __import__(module_name, fromlist=['*'])

#             for name in dir(module):
#                 obj = getattr(module, name)
#                 if callable(obj) and name.startswith("task_"):
#                     task_module.append(f"{module_name}.{name}")
                    
#     app.autodiscover_tasks(task_module)

# @app.task(queue='tasks')
# def send_message(mobile, message):
#     time.sleep(3)
#     return f"sms send to user with {mobile} number and message was: {message}"

# The send_message function can be called in two ways:
# send_message.apply_async(('09123456789', 'this is a test message'))
# send_message.apply_async(kwargs={'mobile':'09123456789', 'message': 'this is new message'})

# @app.task(queue='tasks')
# def task_1():
#     time.sleep(3)
#     return
#
# @app.task(queue='tasks')
# def task_2():
#     time.sleep(3)
#     return
#
# @app.task(queue='tasks')
# def task_3():
#     time.sleep(3)
#     return
#
# @app.task(queue='tasks')
# def task_4():
#     time.sleep(3)
#     return
#
# def handle_tasks():
#     task_2.apply_async(priority=2)
#     task_4.apply_async(priority=4)
#     task_1.apply_async(priority=1)
#     task_3.apply_async(priority=3)
#     task_2.apply_async(priority=2)
#     task_4.apply_async(priority=4)
#     task_1.apply_async(priority=1)
#     task_3.apply_async(priority=3)

app.autodiscover_tasks()
