# Research Report: Tortilla Prices and Minimum Wage Dynamics in Mexico

## 1. Executive Summary
This research explores the historical pricing dynamics of tortillas—a critical staple food in Mexico—from 2007 to 2024. By utilizing time-series forecasting (Auto-ARIMA) and comparative growth analysis against the Mexican General Minimum Wage (Salario Mínimo General), we uncover significant macroeconomic trends regarding inflation, food security, and the purchasing power of the working class.

## 2. Methodology
The analysis was conducted in three primary phases:

### 2.1 Preliminary Exploration and Data Cleaning
- **Dataset**: Daily prices across various states and store types (Mom and Pop stores vs. Supermarkets) were aggregated.
- **Cleaning**: Missing values in the target variable (`Price per kilogram`) were dropped to maintain data integrity. The dataset was subsequently grouped into national monthly averages to form a continuous time-series.

### 2.2 Time-Series Forecasting (ARIMA)
- **Stationarity Testing**: The Augmented Dickey-Fuller (ADF) test revealed that the historical price data was non-stationary, indicating a consistent upward drift due to inflation and underlying economic factors.
- **Auto-ARIMA Selection**: An automated grid search determined the optimal $(p, d, q)$ and seasonal parameters.
- **Forecast**: The fitted model projected prices 24 months into the future, indicating that the upward trajectory of tortilla prices is statistically expected to continue.

### 2.3 Wage vs. Price Growth Comparison
To contextualize the price increases, we compared the growth of the national average tortilla price against the growth of the official Minimum Wage, normalizing both to a base index of 100 in 2007.

## 3. Key Findings

### The "Lost Decade" of Purchasing Power (2007 - 2018)
For the first 11 years of the dataset, the growth of tortilla prices significantly outpaced minimum wage increases. While the minimum wage remained largely stagnant—growing slowly due to conservative economic policies—tortilla prices climbed steadily. This period represents a tangible loss of purchasing power for minimum-wage earners concerning this essential staple.

### The Turnaround (2019 - Present)
Starting in 2019, drastic shifts in wage policies led to aggressive, double-digit percentage hikes in the minimum wage annually. 
- By 2024, the Minimum Wage Index skyrocketed to **492.3%** of its 2007 baseline.
- In contrast, the Tortilla Price Index reached **268.0%** of its 2007 baseline.

This inflection point illustrates a massive reversal: minimum-wage earners today have significantly more purchasing power relative to tortilla prices than they did a decade ago, despite the continuous inflation of food prices.

## 4. Future Work Potential
This foundational research opens several avenues for more advanced prescriptive analytics:

1. **Regional Disparity Analysis**: Mexico is economically diverse. Future studies should break down the ARIMA forecasts and wage comparisons by state (e.g., Northern border states vs. Southern states) to identify regional food security risks.
2. **Causal Impact Modeling**: Utilizing Double Machine Learning (similar to the Omnichannel Equilibrium project) to estimate the causal effect of specific government subsidies, supply chain disruptions (e.g., corn shortages), or international trade tariffs on the final consumer price.
3. **Cross-Elasticity Studies**: Incorporating the prices of substitute goods (e.g., bread, different corn derivatives) to understand consumer behavior shifts when tortilla prices spikes.
4. **Predictive Alert System**: Building a real-time dashboard that flags anomalous price spikes at the municipal level, allowing for targeted economic interventions before crises escalate.
