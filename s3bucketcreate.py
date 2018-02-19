import boto3
import boto3.session
session = boto3.session.Session(profile_name='webscale')
endpoint = 'https://10.68.45.194:8082'
s3 = session.resource(service_name='s3', endpoint_url=endpoint, verify=False)
client = s3.meta.client
s3.Bucket('my-bucket').create()
for bucket in s3.buckets.all():
 print(bucket.name)
