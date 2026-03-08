Sales Forecasting
Step 1: Problem Framing & Forecasting Design

Objective:
	To deine the business context, forecasting objective, data structure, time horizone, evaluation strategy, and success criteria for a multi-product consumer demand forecasting project before commencing data analysis and modelling.
	
Data Source:
	No data used in this step since it is focused on analytical design and problem framing.
	
Steps:
	1. Defined business context and decision use case for an FMCG packaged goods company. 
	2. Identified forecast targets and product-level structure
	3. Locked time granularity and forecast horizon.
	4. Defined evaluation strategy and error metrics.
	5. Established success criteria, assumptions, and known limitations.

Key Decisions:
	Weekly demand forecasting at product/SKU level
	3 FMCG SKUs: ready meals, beverages, and bakery products
	12-week forecast horizon aligned with operational planning cycles
	Walk-forward validation using RMSE and MAPE
	Comparison against naive and season naive baselines

Outputs Created:
	analysis/01_forecasting_brief.xlsx
		Sheets: 1A_Business_Context
				1B_Forecast_Target
				1C_Time_Granularity_Horizon
				1D_Evaluation_Strategy
				1E_Success_Criteria_Assumptions

Next Step:
	Step 2: Data Collection & Data Dictionary