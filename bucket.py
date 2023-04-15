import boto3
from django.conf import settings
from boto3 import s3

class Bucket:
    """
        CDM Bucket manager

        init method creates connection
    """

    def __init__(self):
        session = boto3.session.Session()
        self.conn = session.client(
            aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
            aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
            service_name=settings.AWS_SERVICE_NAME,
            endpoint_url=settings.AWS_S3_ENDPOINT_URL
        )

    def get_objects(self):
        result = self.conn.list_objects_v2(Bucket=settings.AWS_STORAGE_BUCKET_NAME)
        if result.keys().__contains__("Contents"):
            if result["Contents"] :
                return result["Contents"]
        else:
            return None

    def delete_bucket_object(self,key):
        self.conn.delete_object(Bucket=settings.AWS_STORAGE_BUCKET_NAME,Key=key)
        return True

    def download_bucket_object(self,key):
        s3_res=boto3.resource(
            aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
            aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
            service_name=settings.AWS_SERVICE_NAME,
            endpoint_url=settings.AWS_S3_ENDPOINT_URL
            )
        buck=s3_res.Bucket(settings.AWS_STORAGE_BUCKET_NAME)

        buck.download_file(
            key,
            settings.AWS_LOCAL_STORAGES+key
        )

bucket=Bucket()
