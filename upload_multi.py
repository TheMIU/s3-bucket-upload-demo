import os
import boto3

# how to create access key: https://www.youtube.com/watch?v=8wVvbSUjuHo
s3 = boto3.resource('s3',
    aws_access_key_id = 'your access key id',
    aws_secret_access_key = 'your secret access key' )

BUCKET_NAME = 'km2sbucket'
file_path = 'images/'
s3_key = 'uploads/'

for bucket in s3.buckets.all():
    print(bucket.name)
    
# Loop through all files in the specified directory
for root, dirs, files in os.walk(file_path):
    for file in files:
        local_file_path = os.path.join(root, file)
        s3_file_key = os.path.join(s3_key, file)
        with open(local_file_path, 'rb') as f:
            s3.Bucket(BUCKET_NAME).put_object(Key=s3_file_key, Body=f)
        print(f"Uploaded {local_file_path} to {s3_file_key}")

print("Images upload success")