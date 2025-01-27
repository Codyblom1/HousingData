# Manages the ETL process
import logging
from extract_data import extract_data
from transform_data import transform_raw_data



if __name__ == '__main__':
    # extract raw data
    raw_data = extract_data()
    if raw_data:
        logging.info("Successfully extracted raw data.")


    # transform raw data
    transformed_data = transform_raw_data(raw_data)


    #todo save data into s3 bucket

