Sales Forecasting
Step 7: Final Forecast Generation and Interpretation

Objective: 
	To generate final demand forecasts for each SKU using the best-performing models identified during the model evaluation stage and translate the results into operational insights.
	
Data Source:
	Cleaned weekly SKU-level dataset: weekly_sales_by_sku.csv

Steps Performed:
	1. Selected final forecasting model per SKU based on RMSE performance during walk-forward validation.
		Final models used:
			Bakery products: ETS (Additive Trend)
			Beverages: ARIMA (1,1,1)
			Ready meals: ETS (Additive Trend)
	2. Retrained the selected model using the full historical dataset (242 weeks) for each SKU.
	3. Generated 12-week forward forecasts for each product. 
	4. Created visualisations comparing recent historical demand with forecasted demand.
	5. Interpreted forecasts in terms of inventory planning, production planning, and demand volatility. 
	6. Created project dashboard using key insights and visuals.

Key Insights:
	Bakery demand remains relatively stable with moderate fluctuations.
	Beverage demand shows strong upward momentum and higher volatility.
	Ready meals demand shows a gradual downward trend.
	Demand volatility differs significantly across SKUs, justifying different forecasting models.

Outputs Created:
	outputs/07_final_forecasts.csv
	outputs/07B_forecast_overlay_bakery_products.png
	outputs/07B_forecast_overlay_beverages.png
	outputs/07B_forecast_overlay_ready_meals.png
	outputs/Project04_Forecast_Dashboard.pdf
	
Next Step:
	Project packaging and portfolio presentation