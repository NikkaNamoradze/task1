# Task 1 - S3 Bucket Existence Check & Creation

CLI program that takes a bucket name as an argument, checks if it exists, and creates it if it doesn't.

## Setup

```bash
pip install boto3 python-dotenv
```

შექმენით `.env` ფაილი პროექტის root-ში:

```
aws_access_key_id=YOUR_ACCESS_KEY_ID
aws_secret_access_key=YOUR_SECRET_ACCESS_KEY
aws_session_token=YOUR_SESSION_TOKEN
aws_region_name=us-west-2
```

## Usage

```bash
python main.py <bucket_name> [--region us-west-2]
```

## Testing

### 1. ახალი bucket-ის შექმნა (bucket არ არსებობს)

```bash
python main.py my-test-bucket-12345
```

მოსალოდნელი output:
```
Bucket 'my-test-bucket-12345' does not exist. Creating...
Bucket 'my-test-bucket-12345' created successfully.
```

### 2. არსებული bucket-ის შემოწმება (bucket უკვე არსებობს)

გაუშვით იგივე ბრძანება მეორეჯერ:

```bash
python main.py my-test-bucket-12345
```

მოსალოდნელი output:
```
Bucket 'my-test-bucket-12345' already exists.
```

### 3. სხვა რეგიონით შექმნა

```bash
python main.py my-eu-bucket-12345 --region eu-west-1
```
