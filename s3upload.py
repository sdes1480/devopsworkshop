import boto3
import boto3.session
import os
session = boto3.session.Session(profile_name='webscale')
endpoint = 'https://10.68.45.194:8082'
s3 = session.resource(service_name='s3', endpoint_url=endpoint, verify=False)
client = s3.meta.client
for file in os.listdir("/scandir"):
    if file.endswith(".py"):
        print(os.path.join("/scandir", file))
        bucketname='devops'
        obj = s3.Object(bucketname, file)
        obj.upload_file(file)

for bucket in s3.buckets.all():
 print(bucket.name)
