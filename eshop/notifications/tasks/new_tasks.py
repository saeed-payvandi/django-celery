from config.celery_config import app
import sys


@app.task(queue='tasks')
def my_long_runnig_task(has_error):
    if has_error:
        raise ValueError('An error occurred in long runnig task')
    else:
        sys.stdout.write('Long runnig task has been done!')


@app.task(queue='tasks')
def process_result(result):
    sys.stdout.write('Process task result')
    sys.stdout.flush()


@app.task(queue='tasks')
def process_error_result(task_id, exc, traceback):
    sys.stdout.write('>>>>>>>')
    sys.stdout.write(str(exc))
    sys.stdout.write('>>>>>>>')
    sys.stdout.flush()


def run_task(has_error=False):
    my_long_runnig_task.apply_async(args=[has_error], link=[process_result.s()], link_error=[process_error_result.s()])