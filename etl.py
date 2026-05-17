## Imports

import pandas as pd
import subprocess as sp

## Variables

# Files

source_data_file = 'weather.2016.parquet'
wind_speed_data_file = 'wind_dataset.csv'

# Buckets

bucket_name = 'dataops-eu-west-1'
origin_bucket_key = 'origin-data/'
destination_bucket_key = "transformed-data/"

## Commands

# AWS Commands

cmd_get_file = f'aws s3api get-object --bucket {bucket_name} --key {origin_bucket_key}{source_data_file} {source_data_file}'
cmd_put_file = f'aws s3api put-object --bucket {bucket_name} --key {destination_bucket_key}{wind_speed_data_file}'

# System Commands

rm_file = f'rm {source_data_file} {wind_speed_data_file}'

## Download file

try:
    print(f'\nDownloading data frame {source_data_file}\n')
    sp.run(cmd_get_file)
except Exception as e:
    print(f'Unable to downalod data frame {source_data_file}\n \
          Bucket: {bucket_name}\n \
          Bucket key: {origin_bucket_key}\n \
          Error: {e}'
          )

## Main

print(f'\nReading from file {source_data_file}\n')
try:
    data_frame = pd.read_parquet(source_data_file)
except Exception as e:
    print(f'Unable to read {source_data_file}\n \
          Error: {e}')

## Write to file

try:
    
    print(f'Writing to file: {wind_speed_data_file}')
    windspeed_df = pd.read_parquet(source_data_file, filters=[('WindSpeed','<', 7)])
    windspeed_df.to_csv(wind_speed_data_file)

except Exception as e:
    print(f'Cannot write to file {wind_speed_data_file}\nError: {e}')

## Upload

try:
    
    print(f'\nUploading data frame to {bucket_name}/{destination_bucket_key}{wind_speed_data_file}\n')
    sp.run(cmd_put_file)

except Exception as e:
    print(f'Unable to upload data from {wind_speed_data_file} \n \
          Bucket: {bucket_name}\n \
          Bucket key: {destination_bucket_key}\n \
          Error: {e}'
          )
    
## Clean up

print(f'Clean up, removing {source_data_file} and {wind_speed_data_file}')
try:
    
    sp.run(rm_file)

except Exception as e:
    print(f'Clean up failed: {e}')