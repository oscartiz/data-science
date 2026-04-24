import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.tsa.stattools import adfuller
import pmdarima as pm
import warnings
warnings.filterwarnings('ignore')

print("Loading data...")
df = pd.read_csv('data/tortilla_prices.csv')

# Drop missing values
df = df.dropna(subset=['Price per kilogram'])

# Create datetime index
df['Date'] = pd.to_datetime(df[['Year', 'Month', 'Day']])

# Aggregate average national price by month
monthly_price = df.groupby(['Year', 'Month'])['Price per kilogram'].mean().reset_index()
monthly_price['Date'] = pd.to_datetime(monthly_price[['Year', 'Month']].assign(DAY=1))
monthly_price = monthly_price.set_index('Date').sort_index()

# Keep only the price series
ts = monthly_price['Price per kilogram']

print("Running ADF test for stationarity...")
adf_result = adfuller(ts)
print(f'ADF Statistic: {adf_result[0]}')
print(f'p-value: {adf_result[1]}')

print("Fitting Auto-ARIMA model...")
# Use pmdarima to find best parameters
auto_model = pm.auto_arima(ts, start_p=1, start_q=1,
                           max_p=3, max_q=3, m=12,
                           start_P=0, seasonal=True,
                           d=1, D=1, trace=True,
                           error_action='ignore',  
                           suppress_warnings=True, 
                           stepwise=True)

print(auto_model.summary())

print("Forecasting next 24 months...")
forecast_steps = 24
forecast, conf_int = auto_model.predict(n_periods=forecast_steps, return_conf_int=True)

# Create index for forecast
last_date = ts.index[-1]
forecast_index = pd.date_range(start=last_date + pd.DateOffset(months=1), periods=forecast_steps, freq='MS')

forecast_series = pd.Series(forecast.values, index=forecast_index)
lower_series = pd.Series(conf_int[:, 0], index=forecast_index)
upper_series = pd.Series(conf_int[:, 1], index=forecast_index)

# Plotting
sns.set_theme(style="whitegrid")
plt.figure(figsize=(12, 6))

plt.plot(ts, label='Historical Average Price', color='blue')
plt.plot(forecast_series, label='ARIMA Forecast', color='red')
plt.fill_between(forecast_index, lower_series, upper_series, color='red', alpha=0.2, label='95% Confidence Interval')

plt.title('National Average Tortilla Price: Historical & 2-Year Forecast', fontsize=16)
plt.xlabel('Date', fontsize=12)
plt.ylabel('Price per kg (MXN)', fontsize=12)
plt.legend(loc='upper left')

output_path = '/Users/tiz/.gemini/antigravity/brain/b62d5b93-c0e4-4ddd-9305-f182f234878e/arima_forecast.png'
plt.savefig(output_path, dpi=300, bbox_inches='tight')
print(f"Plot saved to {output_path}")

