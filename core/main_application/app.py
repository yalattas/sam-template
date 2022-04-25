import os, requests, json
import boto3

from error import general_error

def lambda_handler(event, context):

    client = boto3.client('ssm')
    env = os.environ.get('ENVIRONMENT')

    try:
        a = 5 / 0
    except Exception as e:
        general_error(e)

    return {
        'statusCode': 200,
        "body": json.dumps(
            {
                "message": "hello world",
            }
        ),
    }
