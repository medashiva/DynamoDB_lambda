import json
import boto3


dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('LoadLogAlerts')

def lambda_handler(event, context):
    '''
    scan will read every item in the table
    '''
    data = table.scan()
    return {
        'statusCode': 200,
        'body': json.dumps(data)
    } 
