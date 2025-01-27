# This script extracts housing census data
import pandas as pd
import requests
#todo use peotry for dependencies management

def extract_data():
    api_key = '79ad9e4fab1bea843637e2f7d1bf3d141b758c41'

    url = "https://api.census.gov/data/2019/acs/acs5"

    params = {
        "get": "NAME,B25077_001E",
        "for": "county:*",
        "in": "state:06",
        "key": api_key
    }

    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        print("hi")
        return data
    else:
        print(f"Error: {response.status_code}")













