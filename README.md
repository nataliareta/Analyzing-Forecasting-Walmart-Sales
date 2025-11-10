# Analyzing-Forecasting-Walmart-Sales

![image alt](https://github.com/nataliareta/Analyzing-Forecasting-Walmart-Sales/blob/608bf36f3c55daca68525194e455b1bb9de5a1d0/Dashboard_Walmart_Sales.jpg)

Here is Walmart sales data, which I've used to create forecasting and a dashboard. This allows for a more detailed and in-depth analysis, where I extensively discuss both internal and external factors influencing the weekly sales.

Features include:
- Store	Date
- Weekly_Sales
- Holiday_Flag
- Temperature
- Fuel_Price
- CPI
- Unemployment

---

##### Sales Forecasting
Developed a robust XGBoost Regressor model to forecast weekly sales for 45 Walmart stores, achieving high predictive accuracy through specialized time series feature engineering. Key Technical Contributions:
1. Time Series Feature Engineering: Engineered critical time-based features, including Weekly Lags and the Sales_Lag_52 feature, which was identified as the most significant predictor (score > 0.81) of sales seasonality.
2. Model Performance: Achieved a strong validation score with a Mean Absolute Error (MAE) of $33,231.84 on the test set, demonstrating the model's high reliability in predicting sales values.
3. Feature Importance Analysis: Discovered that annual seasonality (Sales_Lag_52) and individual store characteristics (e.g., Store_35) were significantly more influential than macro-economic variables (CPI, Unemployment).
4. Model Validation: Confirmed model stability and accuracy through Hyperparameter Tuning and successful visualization of predicted trends against actual sales.

You can open my model predicition :
[![Colab](https://img.shields.io/badge/Colab-F9AB00?style=for-the-badge&logo=googlecolab&color=525252)](https://colab.research.google.com/drive/1RvZ7cyfqavxI9uZGcyR7O1pFBD5WLrgx?usp=sharing)

---

##### Data Analysis
Walmart Sales Data Cleaning & Preprocessing:
- Handled and imputed missing values in external data features (CPI, Unemployment, etc.).
- Confirmed correct data type conversions, especially for the 'Date' column.
- Applied scaling to continuous features (Temperature, Fuel_Price, CPI, Unemployment) for normalization.
- Validated the target column scale (Weekly_Sales) to ensure values were in actual US Dollars (millions), correcting an earlier scaling error.

---

##### Key Insights
The comprehensive analysis, driven by the XGBoost model (MAE $33K) and detailed dashboard review, reveals that sales are overwhelmingly influenced by predictable internal seasonal factors rather than external macroeconomic conditions.
1. Annual Seasonality is the Overwhelming Driver
Sales Lag is King: The Sales_Lag_52 feature (prior year's sales for the same week) was identified as the single most dominant predictor, scoring 0.816 in Feature Importance.
Business Implication: This strongly confirms that annual seasonality and recurring holiday cycles are the most critical factors influencing sales volatility. Forecasting strategies must prioritize this annual pattern.
2. Store Dynamics Outweigh Macroeconomics
Store-Specific Influence: Individual Store ID features (such as Store_35 and Store_4) ranked highly in the model's top predictors. This validates the initial dashboard observation of significant sales disparity among stores.
Macro Weakness: Conversely, macroeconomic variables like CPI, Unemployment, and Fuel Price did not feature in the top 15 predictors.
Business Implication: Differences in local store management, inventory, and demographics have a more powerful, direct impact on weekly sales than national economic fluctuations.
3. Model Performance and Reliability
High Accuracy: The XGBoost model achieved a strong validation score with a Mean Absolute Error (MAE) of $33,231.84 on the testing data.
Trend Capturing: Visual analysis confirmed the model successfully captured the volatile peaks and valleys of sales, demonstrating its reliability in predicting short-term trends within the correct scale.
4. Insight: Data Integrity
Feature-Driven Data Cutting: The necessary removal of initial data rows (via the "data cutting" process) was a direct consequence of creating the Sales_Lag_52 feature.
Integrity Guarantee: This step guaranteed that the model was trained solely on a complete and valid time series dataset, where all essential predictors were present, thereby ensuring the reliability and quality of the final predictions.

---

##### Tools & Technologies
A.Program and Data Analyze (Python Libraries)
- Pandas & NumPy
- XGBoost
- Scikit-learn (sklearn)
- Matplotlib
B. Platform :
- Google Colab
- Vs Code
- Github
- PowerBI

Data Source : https://www.kaggle.com/code/aslanahmedov/walmart-sales-forecasting#Date
