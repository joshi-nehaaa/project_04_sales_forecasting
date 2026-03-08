import pandas as pd
import matplotlib.pyplot as plt

# load actuals
actuals_path = "../data_clean/weekly_sales_by_sku.csv"
df_actual = pd.read_csv(actuals_path)
df_actual["date"] = pd.to_datetime(df_actual["date"])
df_actual = df_actual.sort_values(["sku", "date"])

# load forecasts
forecast_path = "../outputs/07_final_forecasts.csv"
df_fc = pd.read_csv(forecast_path)
df_fc["forecast_date"] = pd.to_datetime(df_fc["forecast_date"], dayfirst=True)

LOOKBACK_WEEKS = 52

print("SKUs:", sorted(df_actual["sku"].unique()))

for sku in sorted(df_actual["sku"].unique()):
    df_sku = df_actual[df_actual["sku"] == sku].copy()
    df_sku = df_sku.sort_values("date")

    # last 52 weeks actuals
    df_hist = df_sku.tail(LOOKBACK_WEEKS)

    # forecasts for sku
    df_sku_fc = df_fc[df_fc["sku"] == sku].sort_values("forecast_date")

    plt.figure()
    plt.plot(df_hist["date"], df_hist["weekly_sales"], label = "Actual (last 52 weeks)")
    plt.plot(df_sku_fc["forecast_date"], df_sku_fc["forecast_weekly_demand"], label = "Forecast (next 12 weeks)")

    plt.title(f"Weekly Demand Forecast (Actual vs Forecast) - {sku}")
    plt.xlabel("Week")
    plt.ylabel("Weekly sales (units)")
    plt.legend()

    file_name = sku.lower().replace(" ", "_")
    output_file = f"../outputs/07B_forecast_overlay_{file_name}.png"
    plt.savefig(output_file, bbox_inches="tight")
    plt.close()

    print("Saved plot:", output_file)