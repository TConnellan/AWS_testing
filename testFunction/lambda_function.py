import json

def lambda_handler(event, context):
    return {
        'statusCode': 200,
        'body': json.dumps('Modified and deployed via ci/cd!')
    }
