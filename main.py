import argparse
from os import getenv

import boto3
from botocore.exceptions import ClientError
from dotenv import load_dotenv

load_dotenv()


def init_client():
    client = boto3.client(
        "s3",
        aws_access_key_id=getenv("aws_access_key_id"),
        aws_secret_access_key=getenv("aws_secret_access_key"),
        aws_session_token=getenv("aws_session_token"),
        region_name=getenv("aws_region_name"),
    )
    client.list_buckets()
    return client


def bucket_exists(client, bucket_name):
    try:
        client.head_bucket(Bucket=bucket_name)
        return True
    except ClientError:
        return False


def create_bucket(client, bucket_name, region=None):
    region = region or getenv("aws_region_name", "us-west-2")
    try:
        client.create_bucket(
            Bucket=bucket_name,
            CreateBucketConfiguration={"LocationConstraint": region},
        )
        return True
    except ClientError as e:
        print(e)
        return False


def main():
    parser = argparse.ArgumentParser(
        description="Check if an S3 bucket exists, create it if not."
    )
    parser.add_argument("bucket_name", help="Name of the S3 bucket")
    parser.add_argument("--region", default=None, help="AWS region (default from .env)")
    args = parser.parse_args()

    client = init_client()

    if bucket_exists(client, args.bucket_name):
        print(f"Bucket '{args.bucket_name}' already exists.")
    else:
        print(f"Bucket '{args.bucket_name}' does not exist. Creating...")
        if create_bucket(client, args.bucket_name, args.region):
            print(f"Bucket '{args.bucket_name}' created successfully.")
        else:
            print(f"Failed to create bucket '{args.bucket_name}'.")


if __name__ == "__main__":
    main()
