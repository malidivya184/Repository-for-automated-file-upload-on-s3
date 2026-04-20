import boto3
import os

s3 = boto3.client('s3')

BUCKET_NAME = 'bucket-for-file-upload1'
FOLDER_PATH = 'images'   # local folder in repo

def upload_folder():
    for root, dirs, files in os.walk(FOLDER_PATH):
        for file in files:
            local_path = os.path.join(root, file)

            # Create S3 path (keep folder structure)
            s3_path = os.path.relpath(local_path, FOLDER_PATH)

            print(f"Uploading {local_path} to {s3_path}")

            s3.upload_file(local_path, BUCKET_NAME, f"images/{s3_path}")

if __name__ == "__main__":
    upload_folder()
