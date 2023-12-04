import boto3

client = boto3.client('s3')

response = client.create_bucket(
    Bucket='pavan-s3-lrn-bkt',
    CreateBucketConfiguration={
        'LocationConstraint': 'ap-south-1'
    }
)