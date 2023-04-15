from bucket import bucket


# TODO: can be asyne
def all_bucket_object_task():
    result = bucket.get_objects()
    return result
