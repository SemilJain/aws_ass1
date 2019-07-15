import boto3

bucket_name = input("Enter the s3 bucket name: ")
object_path = input("Enter the object object_path: ")  #path of the object to download
download_path = input("Enter path to download the object to: ")   #path to download the object to

s3_res = boto3.resource('s3')             

#response = s3_client.list_object_versions(Bucket = bucket_name , Prefix = object_path)

bucket = s3_res.Bucket(bucket_name)               #fetch bucket
versions = bucket.object_versions.filter(Prefix = object_path).all() #fetch a collection of all versions filtering on object
ver_id = list(versions)[1].id                        #getting id of second to latest

bucket.download_file(object_path , download_path , ExtraArgs = {'VersionId' : ver_id})         #download for that version id

