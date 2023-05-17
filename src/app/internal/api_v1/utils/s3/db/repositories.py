
from storages.backends.s3boto3 import S3Boto3Storage
from django.conf import settings

class YandexCloudStorage(S3Boto3Storage):
    bucket_name = settings.AWS_STORAGE_BUCKET_NAME
    location = 'telegram'

    default_acl = 'public-read'
    file_overwrite = True