#This file is used for exploratory data analysis (EDA)
import pandas as pd
import matplotlib.pyplot as plt

# 4A Code:
#Load and clean weekly dataset
data_path = "../data_clean/weekly_sales_by_sku.csv"
df = pd.read_csv(data_path)

from pathlib import Path
Path("../outputs").mkdir(parents=True, exist_ok=True)

print("Loaded dataset shape:", df.shape)
print("\nColumns:", list(df.columns))

# parse date
df["date"] = pd.to_datetime(df["date"], errors="coerce")

# basic checks
print("\nBad dates (failed parsing):", df["date"].isna().sum())
print("Date range:", df["date"].min(), "to", df["date"].max())
print("\nUnique SKUs:", sorted(df["sku"].unique()))

# weeks per SKU (should be equal if fully continuous
weeks_per_sku = df.groupby("sku")["date"].nunique().sort_values(ascending=False)
print("\nWeeks per SKU:")
print(weeks_per_sku)

# Summary stats per SKU
summary = (
    df.groupby("sku")["weekly_sales"]
    .agg(
        weeks = "count",
        mean = "mean",
        std = "std",
        min = "min",
        max = "max",
    )
    .reset_index()
)

# number readability
summary[["mean", "std", "min", "max"]] = summary[["mean", "std", "min", "max"]].round(2)

print("\nSummary stats by SKU:")
print(summary)

# save summary
output_path = "../outputs/04A_summary_stats_by_sku.csv"
summary.to_csv(output_path, index=False)
print("\nSaved summary table to:", output_path)

# 4B Code:
# Plot weekly sales per SKU
for sku in sorted(df["sku"].unique()):
    df_sku = df[df["sku"] == sku].sort_values("date")

    plt.figure()
    plt.plot(df_sku["date"], df_sku["weekly_sales"])
    plt.title(f"Weekly Sales Over Time - {sku}")
    plt.xlabel("Week")
    plt.ylabel("Weekly Sales")

    file_name = sku.lower().replace(" ", "_")
    output_file = f"../outputs/04B_weekly_sales_{file_name}.png"
    plt.savefig(output_file, bbox_inches="tight")
    plt.close()

    print("Saved plot:", output_file)

# 4C Code:
# Rolling average trend diagnostics
ROLLING_WINDOW = 8
for sku in sorted(df["sku"].unique()):
    df_sku = df[df["sku"] == sku].sort_values("date").copy()

    # Rolling average
    df_sku["rolling_mean"] = (
        df_sku["weekly_sales"]
        .rolling(window=ROLLING_WINDOW)
        .mean()
    )

    plt.figure()
    plt.plot(df_sku["date"], df_sku["weekly_sales"], alpha=0.4, label="Weekly Sales")
    plt.plot(df_sku["date"], df_sku["rolling_mean"], linewidth=2, label=f"{ROLLING_WINDOW}-week rolling mean")

    plt.title(f"Weekly Sales with Rolling Trend - {sku}")
    plt.xlabel("Week")
    plt.ylabel("Weekly Sales")
    plt.legend()

    file_name = sku.lower().replace(" ", "_")
    output_file = f"../outputs/04C_rolling_trend_{file_name}.png"
    plt.savefig(output_file, bbox_inches="tight")
    plt.close()

    print("Saved rolling trend plot:", output_file)

# 4D Code:
# Outlier detection (top and bottom weeks)

outlier_summary = []

for sku in sorted(df["sku"].unique()):
    df_sku = df[df["sku"] == sku].sort_values("weekly_sales")

    lowest_weeks = df_sku.head(5)
    highest_weeks = df_sku.tail(5)

    print(f"\n---{sku}---")
    print("Lowest 5 weeks:")
    print(lowest_weeks[["date", "weekly_sales"]])

    print("\nHighest 5 weeks:")
    print(highest_weeks[["date", "weekly_sales"]])

    # store summary for output
    outlier_summary.append({
        "sku": sku,
        "min_weekly_sales" : lowest_weeks["weekly_sales"].min(),
        "max_weekly_sales" : lowest_weeks["weekly_sales"].max()
    })

    outlier_df = pd.DataFrame(outlier_summary)
    output_path = "../outputs/04D_outlier_summary_by_sku.csv"
    outlier_df.to_csv(output_path, index=False)

    print("\nSaved outlier summary to:", output_path)