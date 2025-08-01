import os
import pandas as pd
import requests

# Ensure data directory exists
os.makedirs("../data", exist_ok=True)

REST_URL = (
    "https://gis-mdc.opendata.arcgis.com/datasets/"
    "df6c50202d2c4da2943b4c1ae4cb36d6_0.geojson"
)

def fetch_data():
    print("Fetching data from ArcGIS API...")
    resp = requests.get(REST_URL)
    if resp.status_code not in [200, 202]:
        raise Exception(f"Failed with status {resp.status_code}")
    if resp.status_code == 202:
        print("Received 202 status, waiting for data to be ready...")
        import time
        time.sleep(5)  # Wait 5 seconds for the data to be ready
        resp = requests.get(REST_URL)
        if resp.status_code != 200:
            raise Exception(f"Failed with status {resp.status_code}")
    data = resp.json()
    df = pd.json_normalize(data["features"])
    df.to_csv("../data/low_income_housing_raw.csv", index=False)
    print(f"Saved {len(df)} rows to data/low_income_housing_raw.csv")

if __name__ == "__main__":
    fetch_data()
