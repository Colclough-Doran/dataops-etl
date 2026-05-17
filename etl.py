# Imports
import pandas as pd
import boto3
from io import BytesIO

# Buckets and keys
bucket_name = 'dataops-eu-west-1'
origin_bucket_key = 'origin-data/weather.2016.parquet'
destination_bucket_key = 'transformed-data/wind_dataset.csv'

# Initialize S3 client
s3 = boto3.client('s3')

# Data downstream
try:
    print(f'\nDownloading {origin_bucket_key} from {bucket_name}\n')
    response = s3.get_object(Bucket=bucket_name, Key=origin_bucket_key)
    # Read the Parquet file directly from the S3 response
    data_frame = pd.read_parquet(BytesIO(response['Body'].read()))
    print("File downloaded and loaded successfully.")
except Exception as e:
    print(f'Unable to download or read {origin_bucket_key}\nError: {e}')
    exit(1)

# Process data
try:
    print(f'Filtering data...')
    windspeed_df = data_frame[data_frame['WindSpeed'] < 7]
    csv_data = windspeed_df.to_csv(index=False)
except Exception as e:
    print(f'Cannot process data\nError: {e}')
    exit(1)

# Upload file to S3
try:
    print(f'\nUploading {destination_bucket_key} to {bucket_name}\n')
    s3.put_object(
        Bucket=bucket_name,
        Key=destination_bucket_key,
        Body=csv_data.encode('utf-8')
    )
    print("File uploaded successfully.")
except Exception as e:
    print(f'Unable to upload {destination_bucket_key}\nError: {e}')
    exit(1)

print("Task completed successfully.")