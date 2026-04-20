import boto3

s3 = boto3.client('s3')

s3.upload_file('index.html', 'bucket-for-file-upload1', 'index.html')
