Sales Forecasting
Step 5: Baseline Forecasts & Validation

Objective:
	Establish benchmark forecasting performance using simple baseline models under a walk-forward validation framework

Steps Performed: 
	1. Implemented expanding-window walk-forward validation
		This trained on historical data and forecasted for the next 12 weeks
		It moved forward by one week and was repeated multiple times
	2. Applied naive and rolling mean baseline forecasts
		Naive: assumes demand stays at the last observed level
		Rolling mean: assumes demand equals recent average (8-weeks)
	3. Evaluated performance using RMSE and MAPE across all SKUs
		RMSE: shows absolute error
		MAPE: shows relative error

Key Findings:
	Baseline performance varies by SKUs
	Rolling mean performs better for stable demand categories (Bakery, Ready meals)
	Naive forecasts are more robust for highly volatile demand (Beverages)

Outputs:
	05C_baseline_performance_summary.csv
	
Next Step:
Forecasting models