import pandas as pd

import os

current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(current_dir)

INPUT = r"C:\Users\User\OneDrive\Desktop\MDC Data Analytics\CAPSTONE\LowIncomeHousingUnits_gdb_7804065801993705261.csv"
OUTPUT = os.path.join(project_root, "data", "low_income_housing_cleaned.csv")

def clean_data():
    df = pd.read_csv(INPUT)

    # Identify relevant columns from the actual data
    needed = [
        "Development_Name",
        "Unit_Primary_Street",
        "Unit_City",
        "Unit_Zipcode",
        "Lat",
        "Lon"
    ]
    available = [c for c in needed if c in df.columns]
    df = df[available]

    # Drop rows with missing data
    df = df.dropna(subset=["Unit_Primary_Street", "Lat", "Lon"])

    # Rename columns
    df = df.rename(columns={
        "Development_Name": "property_name",
        "Unit_Primary_Street": "address",
        "Unit_City": "city",
        "Unit_Zipcode": "zip_code",
        "Lat": "lat",
        "Lon": "lon"
    })

    # Reorder columns
    df = df[["property_name", "address", "city", "zip_code", "lat", "lon"]]

    df.to_csv(OUTPUT, index=False)
    print(f"Cleaned data saved with {len(df)} rows to {OUTPUT}")

if __name__ == "__main__":
    clean_data()
