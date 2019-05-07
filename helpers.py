import boto3
import botocore
from config import S3_KEY, S3_SECRET, S3_BUCKET
from flask import abort


s3 = boto3.client("s3", aws_access_key_id=S3_KEY,
                  aws_secret_access_key=S3_SECRET)


def upload_file_to_s3(file, bucket_name, acl="public-read"):
    try:
        s3.upload_fileobj(file, bucket_name, file.filename, ExtraArgs={
            "ACL": acl, "ContentType": file.content_type})

    # Catch all exception
    # need appropriate error codes
    except Exception as e:
        return abort(500)
