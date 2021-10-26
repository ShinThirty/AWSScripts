import argparse

import boto3

parser = argparse.ArgumentParser(description="Delete a S3 bucket.")
parser.add_argument("bucket_name")
args = parser.parse_args()

BUCKET = args.bucket_name
s3 = boto3.resource("s3")
bucket = s3.Bucket(BUCKET)
bucket.object_versions.delete()

bucket.delete()

print(f"Bucket {BUCKET} was deleted successfully.")
