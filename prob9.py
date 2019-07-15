import boto3

dynamodb = boto3.resource('dynamodb' , region_name = "us-east-2")                  
dynamodb_client = boto3.client('dynamodb', region_name='us-east-2')            #used only to check if table exists

try:
	dt_response = dynamodb_client.describe_table(TableName='Games_Semil')
	print("Table already exists")
	table = dynamodb.Table('Games_Semil')                                        #if table already present.. just enter items in table  
except dynamodb_client.exceptions.ResourceNotFoundException:                     # else create table
	table = dynamodb.create_table(
		TableName='Games_Semil',
	    KeySchema=[
	        {
	            'AttributeName': 'gid',
	            'KeyType': 'HASH'
	        },
	        {
	            'AttributeName': 'gname',
	            'KeyType': 'RANGE'
	        }
	    ],
	    AttributeDefinitions=[
	        {
	            'AttributeName': 'gid',
	            'AttributeType': 'N'
	        },
	        {
	            'AttributeName': 'gname',
	            'AttributeType': 'S'
	        },
	        {
	            'AttributeName': 'rating',
	            'AttributeType': 'N'
	        }
	    ],
	    Tags=[
	        {
	            'Key': 'name',
	            'Value': 'Semil'
	        },
	    ],
	    LocalSecondaryIndexes=[
	        {
	            'IndexName': 'gid_rating_index',
	            'KeySchema': [
	                {
	                    'AttributeName': 'gid',
	                    'KeyType': 'HASH'
	                },
	                {
	                    'AttributeName': 'rating',
	                    'KeyType': 'RANGE'
	                }
	                ],
	                'Projection': {
	                'ProjectionType': 'KEYS_ONLY'
	            }
	            
	            },
	            ],
	                BillingMode='PROVISIONED',

	    ProvisionedThroughput={
	        'ReadCapacityUnits': 5,
	        'WriteCapacityUnits': 5
	    }
	)
	table.meta.client.get_waiter('table_exists').wait(TableName='Games_Semil')                  # as it takes time to create table 

	#print(table.item_count)


table.put_item(
   Item={
        'gid': 1,
        'gname': 'fortnite',
        'publisher': 'EpicGames',
        'rating': 9,
        'release_date': '20-12-2012',
        'genre':['fighting','battle_royale']
    }
)

table.put_item(
   Item={
        'gid': 2,
        'gname': 'fifa19',
        'publisher': 'EASports',
        'rating': 8,
        'release_date': '20-12-2011',
        'genre':['sports','strategy']
    }
)

table.put_item(
   Item={
        'gid': 3,
        'gname': 'CS:GO',
        'publisher': 'Steam',
        'rating': 10,
        'release_date': '20-12-2000',
        'genre':['fighting','Multiplayer']
    }
)
print("Added items to table")