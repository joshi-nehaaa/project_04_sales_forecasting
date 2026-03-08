Sales Forecasting
Step 2: Data Collection & Dataset Understanding

Objective:
	To select, inspect, and document the raw dataset, and to align product categories with the defined FMCG SKUs prior to cleaning and modelling.
	
Data Source:
	Store Sales - Time Series Forecasting (Kaggle)

Steps:
	1. Selected and justified a public retail sales dataset (store sales - time series forecasting from Kaggle).
	2. Inspected raw structure using Python (file: 00_data_inspection.py)
		Obtained dataset information such as:
			Number of rows
			Number of columns
			Product Identifier
			Other initial observations
	3. Created a formal data dictionary that describes each column of the dataset. 
	4. Mapped raw product families from the dataset to analytical SKUs with explicit inclusion rules.
		List of all products was obtained using Python.
		Documented in excel by clearly stating if it is included in analysis or not.

Key Decisions:
	Used sales as a proxy for demand.
	Mapped dataset product families to selected SKUs:
		BEVERAGES : Beverages (direct match)
		BREAD/BAKERY: Bakery products (proxy)
		PREPARED MEALS: Ready meals (proxy)
	Excluded non-aligned categories explicitly

Outputs Created:
	src/00_data_inspection.py
	data_raw/store_sales_train.csv
	analysis/01_forecasting_brief.xlsx
		Sheets: 2A_Dataset_Selection
				2B_Raw_Data_Overview
				2C_Data_Dictionary
				2D_Product_Mapping
			
Next Step:
	Data cleaning & time series preparation (python)
