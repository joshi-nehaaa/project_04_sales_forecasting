# this file is for baseline forecasts and validation
# step 5 code
import pandas as pd
import numpy as np
from statsmodels.tsa.holtwinters import ExponentialSmoothing
from statsmodels.tsa.arima.model import ARIMA

# Load cleaned weekly dataset
data_path = "../data_clean/weekly_sales_by_sku.csv"
df = pd.read_csv(data_path)

df["date"] = pd.to_datetime(df["date"])
df = df.sort_values(["sku", "date"]).reset_index(drop=True)

print("Loaded data shape:", df.shape)
print("SKUs:", sorted(df["sku"].unique()))

# validation parameters
FORECAST_HORIZON = 12 # weeks
MIN_TRAIN_WEEKS = 104 # 2 years minimum history

def generate_walk_forward_splits(series, forecast_horizon, min_train_weeks):
    """""
        Generates expanding-window train/test splits for walk-forward validation:
    """
    splits = []
    for end_train in range(min_train_weeks, len(series) - forecast_horizon + 1):
        train = series.iloc[:end_train]
        test = series.iloc[end_train:end_train + forecast_horizon]
        splits.append((train, test))
    return splits

# test walk-forward splits on one SKU
sku_example = "Beverages"
sku_series = df[df["sku"] == sku_example].set_index("date")["weekly_sales"]

splits = generate_walk_forward_splits(
    series = sku_series,
    forecast_horizon = FORECAST_HORIZON,
    min_train_weeks = MIN_TRAIN_WEEKS
)
print(f"\nNumber of walk-forward splits for {sku_example}:", len(splits))

# Inspect the first split
first_train, first_test = splits[0]
print("\nFirst training period:")
print(first_train.index.min(), "to", first_train.index.max())

print("\nFirst test period:")
print(first_test.index.min(), "to", first_test.index.max())

def naive_forecast(train_series, forecast_horizon):
    """""
    Forecasts future values using the last observed value:
    """
    last_value = train_series.iloc[-1]
    return np.repeat(last_value, forecast_horizon)

def rolling_mean_forecast(train_series, forecast_horizon, window=8):
    """""
    Forecasts future values using the mean of the last window observation:
   """
    rolling_mean = train_series.iloc[-window:].mean()
    return np.repeat(rolling_mean, forecast_horizon)

# apply baseline to SKU
sku_example1 = "Beverages"
sku_series = df[df["sku"] == sku_example1].set_index("date")["weekly_sales"]

splits = generate_walk_forward_splits(
    series = sku_series,
    forecast_horizon = FORECAST_HORIZON,
    min_train_weeks = MIN_TRAIN_WEEKS
)
print(f"\nRunning baseline forecasts for {sku_example1}")
print("Number of splits:", len(splits))

# store example forecasts from first split
train, test = splits[0]

naive_pred = naive_forecast(train, FORECAST_HORIZON)
rolling_pred = rolling_mean_forecast(train, FORECAST_HORIZON, window=8)

print("\nFirst test period actual values:")
print(test.values)

print("\nNaive forecast:")
print(naive_pred)

print("\n8-week rolling mean forecast:")
print(rolling_pred)

def rmse(actual, predicted):
    return np.sqrt(np.mean((actual - predicted) ** 2))

def mape(actual, predicted):
    return np.mean(np.abs((actual - predicted) / actual)) * 100

# evaluate baseline models for one SKU
#results = []

#sku_example = "Beverages"
#sku_series = df[df["sku"] == sku_example].set_index("date")["weekly_sales"]

#splits = generate_walk_forward_splits(
    series = sku_series,
    forecast_horizon = FORECAST_HORIZON,
    min_train_weeks = MIN_TRAIN_WEEKS
#)
#for train, test in splits:
#    naive_pred = naive_forecast(train, FORECAST_HORIZON)
#    rolling_pred = rolling_mean_forecast(train, FORECAST_HORIZON, window = 8)

#    results.append({
#        "sku"  : sku_example,
#        "model" : "Naive",
#        "rmse": rmse(test.values, naive_pred),
#        "mape": mape(test.values, naive_pred),
#   })
#    results.append({
#        "sku" : sku_example,
#        "model" : "Rolling Mean_8w",
#        "rmse": rmse(test.values, rolling_pred),
#        "mape": mape(test.values, rolling_pred),
#    })
#results_df = pd.DataFrame(results)
#print("\nSample baseline evaluation results (first 5 rows):")
#print(results_df.head())

# aggregate mean performance across splits
#summary = (
#    results_df
#    .groupby(["sku", "model"])
#    .agg(
#        mean_rmse=("rmse", "mean"),
#        mean_mape=("mape", "mean")
#    )
#    .reset_index()
#)
#print("\nMean baseline performance:")
#print(summary)

# Evaluate baselines for all SKUs
all_results = []

for sku in sorted(df["sku"].unique()):
    sku_series = df[df["sku"] == sku].set_index("date")["weekly_sales"]

    splits = generate_walk_forward_splits(
        series=sku_series,
        forecast_horizon=FORECAST_HORIZON,
        min_train_weeks=MIN_TRAIN_WEEKS
    )

    for train, test in splits:
        naive_pred = naive_forecast(train, FORECAST_HORIZON)
        rolling_pred = rolling_mean_forecast(train, FORECAST_HORIZON, window=8)

        all_results.append({
            "sku": sku,
            "model": "Naive",
            "rmse": rmse(test.values, naive_pred),
            "mape": mape(test.values, naive_pred)
        })

        all_results.append({
            "sku": sku,
            "model": "RollingMean_8w",
            "rmse": rmse(test.values, rolling_pred),
            "mape": mape(test.values, rolling_pred)
        })

all_results_df = pd.DataFrame(all_results)

summary_all = (
    all_results_df
    .groupby(["sku", "model"])
    .agg(
        mean_rmse=("rmse", "mean"),
        mean_mape=("mape", "mean")
    )
    .reset_index()
)

def ets_forecast(train_series, forecast_horizon):
    """""
        Fits an ETS model with additive trend and forecasts future values.
    """
    model = ExponentialSmoothing(
        train_series,
        trend = "add",
        seasonal = None,
        initialization_method = "estimated"
    )
    fitted_model = model.fit()
    forecast = fitted_model.forecast(forecast_horizon)
    return forecast.values

print("\nBaseline performance summary (all SKUs):")
print(summary_all)

output_path = "../outputs/05C_baseline_performance_summary.csv"
summary_all.to_csv(output_path, index=False)

print("\nSaved baseline performance summary to:", output_path)

# step 6 code
# ETS evaluation for one SKU
# ets_results = []

# sku_example = "Beverages"
# sku_series = df[df["sku"] == sku_example].set_index("date")["weekly_sales"]

# splits = generate_walk_forward_splits(
#    series = sku_series,
#    forecast_horizon = FORECAST_HORIZON,
#    min_train_weeks = MIN_TRAIN_WEEKS
#)

# print(f"\nRunning ETS model {sku_example}")

# for train, test in splits:
#    ets_pred = ets_forecast(train, FORECAST_HORIZON)

#    ets_results.append({
#       "sku" : sku_example,
#      "model" : "ETS_AdditiveTrend",
#        "rmse" : rmse(test.values, ets_pred),
#        "mape" : mape(test.values, ets_pred)
#    })
#ets_results_df = pd.DataFrame(ets_results)

#ets_summary = (
#    ets_results_df
#    .groupby(["sku", "model"])
#    .agg(
#        mean_rmse = ("rmse", "mean"),
#        mean_mape = ("mape", "mean")
#    )
#    .reset_index()
#)
#print("\nETS performance summary (Beverages):")
#print(ets_summary)

# ETS evaluation for all SKUs
ets_all_results = []

for sku in sorted(df["sku"].unique()):
    sku_series = df[df["sku"] == sku].set_index("date")["weekly_sales"]

    splits = generate_walk_forward_splits(
        series = sku_series,
        forecast_horizon = FORECAST_HORIZON,
        min_train_weeks = MIN_TRAIN_WEEKS
    )

    for train, test in splits:
        ets_pred = ets_forecast(train, FORECAST_HORIZON)

        ets_all_results.append({
            "sku" : sku,
            "model" : "ETS_AdditiveTrend",
            "rmse": rmse(test.values, ets_pred),
            "mape": mape(test.values, ets_pred)
        })
ets_all_df = pd.DataFrame(ets_all_results)

ets_summary_all = (
    ets_all_df
    .groupby(["sku", "model"])
    .agg(
        mean_rmse=("rmse", "mean"),
        mean_mape=("mape", "mean")
    )
    .reset_index()
)
print("\nETS performance summary (all SKUs):")
print(ets_summary_all)

output_path = "../outputs/06A_ets_performance_summary.csv"
ets_summary_all.to_csv(output_path, index=False)
print("\nSaved ETS performance summary to:", output_path)

# arima
def arima_forecast(train_series, forecast_horizon):
    """""
        Fits an ARIMA (1,1,1) model and forecasts future values.
    """
    model = ARIMA(train_series, order=(1,1,1))
    fitted_model = model.fit()

    forecast = fitted_model.forecast(steps=forecast_horizon)

    return forecast.values

arima_all_results = []

for sku in sorted(df["sku"].unique()):
    sku_series = df[df["sku"] == sku].set_index("date")["weekly_sales"]

    splits = generate_walk_forward_splits(
        series=sku_series,
        forecast_horizon=FORECAST_HORIZON,
        min_train_weeks=MIN_TRAIN_WEEKS
    )

    for train, test in splits:
        try:
            arima_pred = arima_forecast(train, FORECAST_HORIZON)

            arima_all_results.append({
                "sku": sku,
                "model": "ARIMA_1_1_1",
                "rmse": rmse(test.values, arima_pred),
                "mape": mape(test.values, arima_pred)
            })
        except:
            # In case ARIMA fails on a split
            continue

arima_all_df = pd.DataFrame(arima_all_results)

if arima_all_df.empty:
    print("\nARIMA produced no results")
    print("Check arima_forecast()")
else:
    arima_summary_all = (
        arima_all_df
        .groupby(["sku", "model"])
        .agg(
            mean_rmse=("rmse", "mean"),
            mean_mape=("mape", "mean")
        )
        .reset_index()
    )

print("\nARIMA performance summary (all SKUs):")
print(arima_summary_all)

output_path = "../outputs/06B_arima_performance_summary.csv"
arima_summary_all.to_csv(output_path, index=False)
print("\nSaved ARIMA performance summary to:", output_path)

baseline_summary = (
    all_results_df
    .groupby(["sku", "model"])
    .agg(
        rmse=("rmse", "mean"),
        mape=("mape", "mean")
    )
    .reset_index()
)
print("\nBaseline summary (recomputed):")
print(baseline_summary)

# combine all model results
# baseline renamed
baseline_temp = baseline_summary.copy()

# rename ets
ets_temp = ets_summary_all.rename(columns = {
    "mean_rmse" : "rmse",
    "mean_mape" : "mape"
}).copy()

# rename ARIMA
arima_temp = arima_summary_all.rename(columns = {
    "mean_rmse" : "rmse",
    "mean_mape" : "mape"
}).copy()

# combine all
all_models_df = pd.concat([
    baseline_temp[["sku", "model", "rmse", "mape"]],
    ets_temp[["sku", "model", "rmse", "mape"]],
    arima_temp[["sku", "model", "rmse", "mape"]]
], ignore_index=True)

print("\nCombined model comparison:")
print(all_models_df)

# select best model per sku based on lowest RMSE
model_selection = (
    all_models_df
    .sort_values(["sku", "rmse"])
    .groupby("sku", as_index = False)
    .first()
    .reset_index()
)

print("\nSelected best model per SKU:")
print(model_selection)

output_path = "../outputs/06C_model_selection.csv"
model_selection.to_csv(output_path, index=False)
print("\nSaved model selection to:", output_path)

# Step 7
# Final Forecast Generation
print("\nStarting Step 7A — Final Forecast Generation")

FORECAST_HORIZON = 12
final_forecasts = []

# Load model selection file
model_selection = pd.read_csv("../outputs/06C_model_selection.csv")

for _, row in model_selection.iterrows():

    sku = row["sku"]
    model_name = row["model"]

    print(f"\nProcessing SKU: {sku} using {model_name}")

    sku_series = (
        df[df["sku"] == sku]
        .set_index("date")["weekly_sales"]
    )

    if model_name == "ARIMA_1_1_1":
        model = ARIMA(sku_series, order=(1, 1, 1))
        fitted_model = model.fit()
        forecast_values = fitted_model.forecast(steps=FORECAST_HORIZON)

    elif model_name == "ETS_AdditiveTrend":
        model = ExponentialSmoothing(
            sku_series,
            trend="add",
            seasonal=None,
            initialization_method="estimated"
        )
        fitted_model = model.fit()
        forecast_values = fitted_model.forecast(FORECAST_HORIZON)

    else:
        raise ValueError(f"Unknown model: {model_name}")

    last_date = sku_series.index.max()
    forecast_dates = pd.date_range(
        start=last_date + pd.Timedelta(weeks=1),
        periods=FORECAST_HORIZON,
        freq="W-SUN"
    )

    for date, value in zip(forecast_dates, forecast_values):
        final_forecasts.append({
            "sku": sku,
            "model_used": model_name,
            "forecast_date": date,
            "forecast_weekly_demand": float(value)
        })

final_forecasts_df = pd.DataFrame(final_forecasts)

output_path = "../outputs/07_final_forecasts.csv"
final_forecasts_df.to_csv(output_path, index=False)

print("\nSaved final forecasts to:", output_path)
print("\nTotal forecast rows:", len(final_forecasts_df))
print(final_forecasts_df.head())