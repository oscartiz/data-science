# Job Salary Prediction

This sub-project implements a high-performance Deep Neural Network (DNN) to predict professional salaries based on a dataset of 250,000 job records.

## Project Overview
The goal was to build a robust regression model that can accurately estimate annual salary based on:
- Years of Experience
- Education Level
- Industry Sector
- Company Size
- Remote Work Status
- Specific Skills and Certifications

## Tech Stack
- **Python 3**
- **PyTorch**: Deep Learning framework for the DNN.
- **Scikit-Learn**: Data preprocessing (One-Hot Encoding, Scaling).
- **Matplotlib/Seaborn**: Data visualization and performance plotting.

## Getting Started
1. **Environment**:
   ```bash
   cd job_salary_prediction
   source .venv/bin/activate
   ```
2. **Analysis**:
   Open `salary_prediction_dnn.ipynb` to view the exploratory data analysis, the Grid Search results, and the final model training.

## Dataset
The dataset was sourced via `kagglehub` from `nalisha/job-salary-prediction-dataset`. It features 250,000 samples with zero missing values.
