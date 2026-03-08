Sales Forecasting
Step 6: Forecasting Models (ETS & ARIMA)

Objective: 
	To test statistical forecasting models (ETS and ARIMA) under the established walk-forward validation framework and selecting the best performing model per SKU.
	
Data Source: 
	Cleaned weekly SKU-level dataset (weekly_sales_by_sku.csv) produced in Step 3. 
	
Steps Performed:
	1. Implemented ETS (additive trend, non-seasonal) and evaluated via walk-forward validation.
	2. Implemented ARIMA (1,1,1) (non-seasonal) and evaluated via walk-forward validation
	3. Compared model performance against baseline models (Naive and 8-week rolling mean)
	4. Selected final model per SKU based on lowest mean RMSE
	5. Recorded modelling limitations and diagnostic notes (warnings, convergence behaviour)

Key Findings: 
	Each SKU against best performing model is as follows:
		Bakery products - ETS: modest improvement vs baselines
		Beverages - ARIMA: improved RMSE and MAPE compared to ETS and baselines
		Ready meals - ETS: small but consistent improvements
	Overall, baseline models were strong; improvements from statistical models were incremental for stable SKUs.
	
Outputs:
	outputs/06A_ets_performance_summary.csv
	outputs/06B_arima_performance_summary.csv
	outputs/06C_model_selection.csv

Next Step:
	Train selected models on full history and generate 12-week forward forecasts per SKU. 

