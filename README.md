The script uses boto and will use IAM roles to access AWS resources.
Downstream from s3 the data from weather.2016.parquet
The data will be read, processed and written to wind_dataset.csv in memory.
Once complete, wind_dataset.csv will be uploaded to the s3 bucket dataops-eu-west-1/transformed-data/