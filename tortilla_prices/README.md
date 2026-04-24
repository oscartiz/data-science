# Tortilla Prices Analysis

This sub-project explores the historical data of tortilla prices in Mexico (2007-2024), performs a time-series forecast using ARIMA, and compares the price growth against the historical minimum wage in Mexico.

## Contents
- `data/`: Contains the datasets used (tortilla prices).
- `tortilla_prices_analysis.ipynb`: A consolidated Jupyter Notebook containing:
  - Preliminary Data Exploration
  - ARIMA Statistical Forecasting Model
  - Minimum Wage vs. Tortilla Price Growth Comparison
- `run_arima.py`: Script to generate the ARIMA model forecast.
- `run_wage_comparison.py`: Script to generate the wage vs. price comparison.
- `REPORT.md`: An extensive report summarizing the findings, methodology, and future research potential.

## Quick Start
1. Ensure your `.venv` is activated and dependencies are installed (`pandas`, `matplotlib`, `seaborn`, `pmdarima`, `statsmodels`).
2. Run the `tortilla_prices_analysis.ipynb` notebook to see the full data pipeline and visualizations.
