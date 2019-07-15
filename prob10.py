import boto3
from boto3.dynamodb.conditions import Key


dynamodb = boto3.resource('dynamodb', region_name='us-east-2')
table = dynamodb.Table('Games_Semil')                     #fetch table for querying
gid = 2                                                  #hardcoded as stated in the problem
query_response = table.query(
    IndexName='gid_rating_index',                          #indexing using local secondary index 
    Select='ALL_PROJECTED_ATTRIBUTES',
    KeyConditionExpression=Key('gid').eq(gid)               #checking for id match
)
for item in query_response['Items']:
    print("gname: {}, rating: {}".format(item['gname'], item['rating']))                  #printing only name and rating


