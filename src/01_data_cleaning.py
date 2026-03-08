# This file handles filtering selected SKUs, date parsing, aggregation and data preparation
import pandas as pd

# Load raw data
data_path = "../data_raw/store_sales_train.csv"
df = pd.read_csv(data_path)
print("Initial shape:", df.shape)

# Define product families
selected_families = [
    "BEVERAGES",
    "BREAD/BAKERY",
    "PREPARED FOODS"
]

# Filter dataset to the selected product families
df_filtered = df[df["family"].isin(selected_families)].copy()

print("Filtered shape:", df_filtered.shape)

print("\nRemaining product families:")
print(sorted(df_filtered["family"].dropna().unique()))

# Parse date column to datetime
df_filtered["date"] = pd.to_datetime(df_filtered["date"], format="%Y-%m-%d", errors="coerce")

# Check if any dates failed to parse
num_bad_dates = df_filtered["date"].isna().sum()
print("\nBad dates (failed parsing):", num_bad_dates)

# Sort by date
df_filtered = df_filtered.sort_values(["date", "store_nbr", "family"]).reset_index(drop = True)
print("Data sorted. First date:", df_filtered["date"].min(), "Last date:", df_filtered["date"].max())

# Check for negative sales
neg_sales_count = (df_filtered["sales"] < 0).sum()
print("Negative sales count:", neg_sales_count)

# Check missing values
print("\nMissing values per column:")
print(df_filtered.isna().sum())

# Check duplicates on the key columns
dup_count = df_filtered.duplicated(subset=["date", "store_nbr", "family"]).sum()
print("\nDuplicate rows on (date, store_nbr, family):", dup_count)

# Map raw families to analysis SKUs
sku_map = {
    "BEVERAGES": "Beverages",
    "BREAD/BAKERY": "Bakery products",
    "PREPARED FOODS": "Ready meals"
}

df_filtered["sku"] = df_filtered["family"].map(sku_map)
print("\nSKU values after mapping:", sorted(df_filtered["sku"].unique()))

# Aggregate daily -> weekly totals per SKU (across all stores)
weekly_sku = (
    df_filtered
    .groupby(["sku", pd.Grouper(key="date", freq="W-SUN")], as_index=False)
    .agg(
        weekly_sales=("sales", "sum"),
        weekly_onpromo=("onpromotion", "sum") #reference only, not modelling
    )
)

print("\nWeekly dataset shape:", weekly_sku.shape)
print(weekly_sku.head())

#integrity checks
print("\nWeekly date range:",
      weekly_sku["date"].min(), "to", weekly_sku["date"].max())

print("\nWeeks per SKU:")
print(weekly_sku.groupby("sku")["date"].nunique())

print("\nAny missing values?")
print(weekly_sku.isna().sum())

# Time-series continuity checks
print("\nWeeks per SKU:")
print(weekly_sku.groupby("sku")["date"].nunique())

# Created expected weekly date range
full_week_range = pd.date_range(
    start = weekly_sku["date"].min(),
    end = weekly_sku["date"].max(),
    freq = "W-SUN"
)

# Check missing weeks per SKU
for sku in weekly_sku["sku"].unique():
    sku_weeks = weekly_sku.loc[weekly_sku["sku"] == sku, "date"]
    missing_weeks = set(full_week_range) - set(sku_weeks)
    print(f"\nMissing weeks for {sku}: {len(missing_weeks)}")

# Check duplicates at weekly level
dup_weekly = weekly_sku.duplicated(subset=["sku", "date"]).sum()
print("\nDuplicate weekly rows (sku, date):", dup_weekly)

# Save cleaned weekly dataset
output_path = "../data_clean/weekly_sales_by_sku.csv"
weekly_sku.to_csv(output_path, index=False)

print("\nCleaned weekly dataset saved to:", output_path)
