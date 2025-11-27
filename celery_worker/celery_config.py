from decouple import config

broker_url = config('BROKER_URL', default='redis://redis:6379/0')
result_backend = config('RESULT_BACKEND', default='redis://redis:6379/0')