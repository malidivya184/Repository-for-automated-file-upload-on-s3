import boto3
import os

s3 = boto3.client('s3')

BUCKET_NAME = 'bucket-for-file-upload1'
FOLDER_PATH = 'images'

for file in os.listdir(FOLDER_PATH):
    if file.lower().endswith(('.png', '.jpg', '.jpeg')):
        local_path = os.path.join(FOLDER_PATH, file)
        s3_key = f"images/{file}"

        print(f"Uploading {file}...")
        s3.upload_file(local_path, BUCKET_NAME, s3_key)

print("Upload completed")
