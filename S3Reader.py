import json
import boto3


def lambda_handler(event, context):
    bucket = 'ser-addresses'
    key = 'addresses.csv'
    s3 = boto3.client('s3')
    response = s3.get_object(Bucket=bucket, Key=key)
    file_content = response['Body'].read().decode('utf-8')
    print(file_content)
