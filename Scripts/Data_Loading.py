import boto3
from config import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_S3_BUCKET_NAME

def upload_to_s3(df, file_name):
    s3 = boto3.client(
        's3',
        aws_access_key_id=AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY
    )
    csv_buffer = df.to_csv(index=False)
    s3.put_object(Bucket=AWS_S3_BUCKET_NAME, Key=file_name, Body=csv_buffer)
