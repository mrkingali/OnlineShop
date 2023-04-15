from bucket import bucket
from celery import shared_task

# TODO: can be asyne
def all_bucket_object_task():
    result = bucket.get_objects()
    return result

@shared_task
def delete_object_bucket(key):
    bucket.delete_bucket_object(key)

@shared_task
def download_bucket_object(key):
    bucket.download_bucket_object(key)