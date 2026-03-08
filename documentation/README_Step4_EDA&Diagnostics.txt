Sales Forecasting
Step 4: Exploratory Data Analysis & Diagnostics

Objective:
	To explore and understand weekly demand patterns across selected FMCG SKUs prior to forecasting, focusing on trend behaviour, volatility, seasonality, and the presence of outliers.

Data Source:
	Cleaned weekly SKU-level dataset generated in Step 3:
		weekly_sales_by_sku.csv

Steps Performed:
	1. Loaded and validated cleaned weekly dataset
	2. Generated summary statistics by SKU-level
	3. Visualised weekly sales trends for each SKU
	4. Applied rolling average smoothing to identify underlying trends
	5. Identified and reviewed extreme high and low demand weeks
	6. Assessed time-series continuity and data quality
	
Key Findings:
	Beverages exhibit the highest average demand and the greates volatility, with strong upward growth and pronounced spikes.
	Bakery products show a steady upward trend with moderate variability, indicating relatively predictable demand. 
	Ready meals demonstrate lower overall demand levels with limited volatility and slower growth.
	Rolling averages reveal clear long-term trends across all SKUs, with no evidence of structural breaks. 
	Extreme weekly values appear plausible and consistent with observed demand behaviour rather than data errors. 
	
Outputs Created:
	SKU-level summary statistics table
	Weekly time-series plots per SKU
	Rolling trend diagnostics plots
	Outlier summary table
	
Next Step:
	Baseline forecasts & validation framework