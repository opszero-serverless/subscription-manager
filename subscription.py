import json
import boto3
import stripe

DynamoDBTable = 'cashier'


class Subscription(object):
    def get_subscription(self):
        if

    def subscribe(self, id, product, email, plan):

    def unsubscribe(self, id, product):
        pass

def handler(event, context):
    if event['Method'] == 'POST':
        pass
    elif event['Method'] == 'GET':
        pass
    else:
        return {
            'StatusCode': 404,
            'Message': 'Unknown event action'
        }
