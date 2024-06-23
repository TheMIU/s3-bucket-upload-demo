import boto3

# how to create access key: https://www.youtube.com/watch?v=8wVvbSUjuHo
s3 = boto3.resource('s3',
    aws_access_key_id = 'your access key id',
    aws_secret_access_key = 'your secret access key' )

BUCKET_NAME = 'km2sbucket'

# check all bucket names
for bucket in s3.buckets.all():
    print(bucket.name)

# create bucket object
bucket = s3.Bucket(BUCKET_NAME)

# delete everything inside the bucket
bucket.objects.all().delete()

print(f"{BUCKET_NAME} is empty now")