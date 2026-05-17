The python script will download the file weather.2016.parquet file from the s3 bucket dataops-eu-west-1/origin-data/
Then it will read from the file. 
Filter the data based on wind speed.
The filtered data will be stored in wind_dataset.csv
wind_dataset.csv will be placed in the s3 bucket dataops-eu-west-1/transformed-data/
When it is complete it will delete both files from local storage