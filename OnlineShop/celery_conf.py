import os
from datetime import timedelta

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'OnlineShop.settings')

celery_app = Celery('OnlineShop')
celery_app.autodiscover_tasks()

celery_app.conf.broker_url = 'amqp://'
celery_app.conf.result_backend = 'rpc://'
celery_app.conf.task_serializer = 'json'
celery_app.conf.result_serializer = 'pickle'
celery_app.conf.accept_content = ['json', 'pickle']
celery_app.result_expires = timedelta(days=1)
celery_app.task_always_eager = False
celery_app.worker_prefetch_multiplier = 4
