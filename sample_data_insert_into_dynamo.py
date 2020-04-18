import json
import boto3
import datetime


dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('LoadLogAlerts')

def lambda_handler(event, context):

    for i in range(120):
            Filename = "{}.dat".format(datetime.datetime.now())
            date = "{}".format(datetime.datetime.now())
            LoadStatus = 'True' if i % 2 else 'False'
            New_column = 'impossible' if i % 2 else 'possible'
            input_data = {'Filename':Filename,'date':date,'LoadStatus':LoadStatus,'New_column':New_column}
            table.put_item(Item=input_data)
            
      return {
        'statusCode': 200,
        'body': json.dumps(data)
    }
