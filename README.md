# Task 1 - S3 Bucket Existence Check & Creation

CLI program that takes a bucket name as an argument, checks if it exists, and creates it if it doesn't.

## Setup

```bash
pip install -r requirements.txt
cp .env.example .env
# Fill in your AWS credentials in .env
```

## Usage

```bash
python main.py <bucket_name> [--region us-west-2]
```

### Examples

```bash
# Check and create bucket
python main.py my-unique-bucket

# Specify region
python main.py my-unique-bucket --region eu-west-1
```

## How it works

1. Initializes S3 client using credentials from `.env`
2. Checks if the bucket exists using `head_bucket`
3. If it exists — prints that the bucket already exists
4. If it doesn't exist — creates it and confirms
