import json
import boto3


dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('LoadLogAlerts')



'''
https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/ReservedWords.html

Projection Expressions : is a string that identifies the attributes that you want. To retrieve a single attribute, specify its name. For multiple attributes, the names must be comma-separated
in a layman way: attribute is your table columns.


'''

def lambda_handler(event, context):
    '''
    scan will read every item in the table
    '''
    data = table.scan() # it will read all the data 
    --------------------------*** Condition Based ***-----------------------------------------
    '''
    column name is LoadStatus
    Values are True and False in my table
    fetching only True records
    '''
    fe = Key('LoadStatus').eq('True')# where condition preparation
    data = table.scan(
        FilterExpression=fe, #where condition
        )
    --------------------------*** Condition based End ***----------------------------------------
    
        --------------------------*** Condition and select limited columns Based ***-----------------------------------------
    '''
    column name is LoadStatus
    Values are True and False in my table
    fetching only True records
    '''
    fe = Key('LoadStatus').eq('True') # where condition preparation
    pe = "Filename" # attributes or columns you want to return in the result.. silmilar to select column name in sql
    data = table.scan(
        FilterExpression=fe, #where condition
        ProjectionExpression=pe,
        )
    --------------------------*** Condition and select limited columns Based End ***----------------------------------------
    
    
    return {
        'statusCode': 200,
        'body': json.dumps(data)
    } 
