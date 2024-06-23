import os
import boto3

# how to create access key: https://www.youtube.com/watch?v=8wVvbSUjuHo
s3 = boto3.resource('s3',
    aws_access_key_id = 'your access key id',
    aws_secret_access_key = 'your secret access key' )

BUCKET_NAME = 'km2sbucket'
file_path = 'me.jpg'
s3_key = 'uploads/me.jpg'

for bucket in s3.buckets.all():
    print(bucket.name)
    
with open (file_path, 'rb') as file:
    s3.Bucket(BUCKET_NAME).put_object(Key=s3_key, Body=file)
    
print("Image upload success")
