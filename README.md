Python Data Processing Script

Overview

This Python script processes weather data stored in a Parquet file (weather.2016.parquet) from an S3 bucket. It reads the data, applies transformations, and writes the processed output as a CSV file (wind_dataset.csv) in memory. The final CSV is then uploaded to the S3 bucket at dataops-eu-west-1/transformed-data/.

Key Features

AWS Integration: Uses boto3 to interact with AWS services.
IAM Roles: Relies on IAM roles for secure access to AWS resources (S3, etc.).
In-Memory Processing: Reads, processes, and writes data in memory for efficiency.
Output: Uploads the transformed CSV (wind_dataset.csv) to the specified S3 path.

Dependencies

Python 3.x
boto3 (AWS SDK for Python)
pandas (for Parquet/CSV handling)
pyarrow or fastparquet (for Parquet file support)

Usage

IAM Configuration:
Ensure the script runs with an IAM role that has permissions to:

Read from the source S3 bucket (e.g., dataops-eu-west-1/).
Write to the destination S3 path (dataops-eu-west-1/transformed-data/).

Input/Output:
Input: weather.2016.parquet (from S3).
Output: wind_dataset.csv (uploaded to dataops-eu-west-1/transformed-data/).

Notes

The script assumes the input Parquet file is structured as expected (e.g., contains weather data with wind-related columns).
Error handling (e.g., missing files, permissions) should be added for production use.
