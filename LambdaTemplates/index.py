import json
import datetime
import boto3
import os          ## to get the env variables


def lambda_handler(event, context):

    status = 200
    response_body = []
    a = 0

    data = {
        'output': 'Hello World',
        'timestamp': datetime.datetime.utcnow().isoformat()
    }

    try:
        print (">>>>> starting a lambda function...")
        a += 1
        response_body = { 'value': 'a' }
        
    except Exception as e:
        print(">>>>> sorry! something went wrong!! %e", e)
        status = 502
        

    finally:
        print(">>>>> executed successfully lambda function...")
        return {
            "statusCode" : status,
            "headers" : {
                "Message":("function execution is complete. Here is the value {}".format(a))
            },
            "body" : response_body
        }
