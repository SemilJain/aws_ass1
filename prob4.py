import json

def lambda_handler(event, context):
    # TODO implement
    return {
        'statusCode': 200,
        'body': event["name"]                   #displaying name passed in url by api gateway
    }




#https://joa59ubui0.execute-api.us-east-2.amazonaws.com/training_stage?name=semil        ----> url generated