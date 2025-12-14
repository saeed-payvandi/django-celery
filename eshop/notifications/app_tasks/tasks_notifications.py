from config.celery_config import app

@app.task(queue='tasks')
def task_1():
    pass


