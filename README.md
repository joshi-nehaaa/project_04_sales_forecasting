# Project 04 — Demand Forecasting for FMCG Products

**Objective:**\
This project develops a demand forecasting workflow for a mid-sized FMCG company across three product categories: bakery products, beverages, and ready meals.
The goal is to evaluate forecasting models using historical weekly sales data and generate short-term demand forecasts to support production planning and inventory management.

**Tools:**\
Python, Excel

**Key Findings**\
- Forecast accuracy varies significantly across product categories.
- ETS models perform well for stable demand series.
- ARIMA performs better for more volatile demand patterns.
- No single forecasting model performs best across all SKUs.
- Final model selection:
    Bakery products: ETS
    Beverages: ARIMA
    Ready meals: ETS

**Repo Map:**\
<details>
<summary>📁 analysis/</summary>
- project_04_sales_forecasting_analysis.xlsx
</details>

<details>
<summary>📁 data_clean/</summary>
- weekly_sales_by_sku.csv 
</details>

<details>
<summary>📁 data_raw/</summary>
- store_sales_train.csv
</details>

<details>
<summary>📁 documentation/</summary>
- README_Step1_Scope&ForecastDesign
- README_Step2_DataCollection&Dictionary
- README_Step3_DataCleaning&Prep
- README_Step4_EDA&Diagnostics
- README_Step5_Baselines&Validation
- README_Step6_Modeling
- README_Step7_FinalForecasting
</details>

<details>
<summary>📁 outputs/</summary>
- 04A_summary_stats_by_sku
- 04B_weekly_sales_bakery_products
- 04B_weekly_sales_beverages
- 04B_weekly_sales_ready_meals
- 04C_rolling_trend_bakery_products
- 04C_rolling_trend_beverages
- 04C_rolling_trend_ready_meals
- 04D_outlier_summary_by_sku
- 05C_baseline_performance_summary
- 06A_ets_performance_summary
- 06B_arima_performance_summary
- 06C_model_selection
- 07_final_forecasts
- 07B_forecast_overlay_bakery_products
- 07B_forecast_overlay_beverages
- 07B_forecast_overlay_ready_meals
- Project04_Forecast_Dashboard
- project_04_sales_forecasting_case_brief
</details>

<details>
<summary>📁 src/</summary>
- 01_data_cleaning.py
- 02_eda.py
- 03_validation_framework.py
- 04_forecast_visuals.py
</details>

**Portfolio:** \
Explore this project and others on my Notion portfolio: https://joshi-nehaaa.notion.site/Portfolio-Neha-Joshi-2ca1601f482680ec84decf9f70295ce3?source=copy_link
