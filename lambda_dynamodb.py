import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('LoadLogAlerts')


def lambda_handler(event, context):
    '''
    Points to remember
    1. Create API Gateway
    2. Crate a role to talk with dynamodb
    3. IMP:While creating dynamodb , if we take sort column, we should pass primary and sort key in get method
    '''
    if event['httpMethod'] == 'GET':
        filename = str(event['queryStringParameters']['Filename'])
        date = str(event['queryStringParameters']['date'])
        q_string = {"Filename": filename, "date": date}
        data = table.get_item(Key=q_string)
    else:
        data_p = json.loads(event['body'])
        table.put_item(Item=data_p)

    return {
        'statusCode': 200,
        'body': json.dumps(data)
    }