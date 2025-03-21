"""
This script is a simple example of using data that is predefined in  a csv in an ETL method. We will be transforming the
data into a category where the price is less than 1m to stay on budget.
"""
import pandas as pd
from pathlib import Path
import logging

# Extract
def extract_data():
    #todo: Implement data pull from a restapi instead with housing data.

    # This dynamically finds the absolute file path to the csv no matter the cwd avoiding issues finding the csv.
    repo_root = Path(__file__).resolve().parent
    csv_data_path = repo_root / "data/mock_housing_data.csv"

    # Read raw data into a dataframe from csv and return
    df = pd.read_csv(csv_data_path)
    logging.info(f"Successfully extracted {len(df)} rows of data.")
    return df


# Transform
def transform_data(df):
    #todo: Implement more filters such as address, bedrooms, bathrooms

    # filter by houses in a specific zip code & the value.
    df = df.loc[:, ["value", "rooms"]]

    # Filter by houses under 1 million
    df = df.loc[(df["value"] < 1000000) & (df["rooms"] > 2), ["value", "rooms"]]
    return df

# Load
def load_data(filtered_df):
    #todo: Load data into a db file instead of csv

    repo_root = Path(__file__).resolve().parent
    csv_data_path = repo_root / "data/filtered_housing_data"

    logging.info("Starting loading filtered data into csv.")
    filtered_df.to_csv(csv_data_path, index=False)


def main():
    # Extract the raw data from csv in data folder
    raw_data = extract_data()

    # Transform the data into selected price range and zip code.
    filtered_df = transform_data(raw_data)

    # Load the data into a new csv
    load_data(filtered_df)
    logging.info("ETL Script finished successfully.")


if __name__ == "__main__":
    # Extract the raw data from csv in data folder
    logging.info("Starting housing ETL script.")

    main()

#todo: Implement poetry for dependency management
#todo: set up airflowpoetry
#todo: install poetry for dependnecies
