AWS_ACCESS_KEY_ID = 'DO00BDFBGJ2BNYKFC7HM'
AWS_SECRET_ACCESS_KEY = 'nnntXpz1z516FALmwPae2kuNNbaS0wq9sVJUJkkThBw'
AWS_STORAGE_BUCKET_NAME = 'yeikabeautyart'
AWS_S3_ENDPOINT_URL = 'https://nyc3.digitaloceanspaces.com' 

AWS_S3_OBJECTS_PARAMETERS = {
    "CacheControl": "max-age=86400"
}
AWS_LOCATION = 'https://yeikabeautyart.nyc3.digitaloceanspaces.com'


DEFAULT_FILE_STORAGE = "config.cdn.backends.MediaRootS3Boto3Storage"
STATICFILES_STORAGE= "config.cdn.backends.StaticRootS3Boto3Storage"