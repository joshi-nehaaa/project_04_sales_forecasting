Sales Forecasting
Step 3: Data Cleaning & Time-Series Preparation

Objective:
	Prepare clean, continuous weekly time series at SKU level aligned with the forecasting design.

Data Source:
	Store Sales - Time Series Forecasting (Kaggle)

Steps:
	1. Filtered raw data to selected FMCG SKUs
		Included BEVERAGES, BREAD/BAKERY, PREPARED FOODS. Excluded all others
		Used pandas .isin() for filtering family column
	2. Parsed and validated date fields
		Used pd.to_datetime
		Obtained first and last date in the dataset. 
	3. Aggregated daily store-level sales to weekly SKU-level totals
	4. Checked continuity of weeks and duplicates
		Obtained total weeks per each SKU
		Checked for missing and duplicate weeks
	5. Saved modelling-ready dataset

Key Decisions:
	Aggregated across stores
	Weekly frequency (W-SUN)
	Sales used as proxy for demand

Outputs Created:
	src/01_data_cleaning.py
	data_clean/weekly_sales_by_sku.csv
	analysis/01_forecasting_brief
		Sheets: 3A_Filtering
				3B_Date_Parsing_Checks
				3C_Weekly_Aggregation
				3D_Time_Series_Integrity

Next Step:
	Exploratory Data Analysis & Diagnostics
