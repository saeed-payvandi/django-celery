from config.celery_config import app
from celery import chain

@app.task(queue='tasks')
def custom_sum(num1, num2):
    return num1 + num2

@app.task(queue='tasks')
def power(num):
    if num == 5:
        raise ValueError('Value can not be 5')
    
    return num ** 2


def run_tasks():
    task_chain = chain(custom_sum.s(2, 3), power.s())
    task_chain_result = task_chain.apply_async()
    task_chain_result.get()