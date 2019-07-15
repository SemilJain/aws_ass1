import json
import os
import boto3

def lambda_handler(event, context):
    
    s3 = boto3.resource('s3')
    destinationBucket = s3.Bucket(os.environ['destinationBucket'])

    key = event['Records'][0]['s3']['object']['key']               #getting the key of the object to copy 
    copy_source = {
    'Bucket': event['Records'][0]['s3']['bucket']['name'],          #creating dict for bucket and key 
    'Key': key
    }
    
    obj = destinationBucket.Object(key)
    obj.copy(copy_source)                                 #copying into dest
    
    return {
        'statusCode': 200,                               #success status
        }

