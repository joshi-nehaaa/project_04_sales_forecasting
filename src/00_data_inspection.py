# This file is used for initial data inspection, schema understanding & category discovery
import pandas as pd

# Load raw data
data_path = "../data_raw/store_sales_train.csv"
df = pd.read_csv(data_path)

# Count observations per product family
family_counts = df["family"].value_counts()

print(family_counts)

# Basic structural checks
print("Shape of dataset:", df.shape)
print("\nColumn names:")
print(df.columns)

print("\nFirst 5 rows:")
print(df.head())

print("\nData types:")
print(df.dtypes)

# View all unique product families
product_families = df["family"].unique()

print("Number of unique product families:", len(product_families))
print("\nProduct families:")
print(product_families)