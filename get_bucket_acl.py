import boto3

client = boto3.client('s3')

response = client.get_bucket_acl(
    ExpectedBucketOwner='pavan-s3-lrn-bkt'
)
