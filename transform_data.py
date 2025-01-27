import pandas as pd


def transform_raw_data(raw_data):
    columns = raw_data[0]
    rows = raw_data[1:0]
    df = pd.DataFrame(rows, columns=columns)
    print(df)
