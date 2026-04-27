# Research Report: Job Salary Prediction DNN

## 1. Executive Summary
This project successfully developed a Deep Neural Network (DNN) capable of predicting annual salaries with an **R-squared score of 0.9745**. By utilizing a Two-Phase Grid Search optimization, we identified a high-capacity architecture that minimizes prediction error while remaining computationally efficient for laptop-based training.

## 2. Methodology

### 2.1 Data Processing
The dataset (250,000 records) was preprocessed using a `ColumnTransformer` pipeline:
- **Numerical Features** (`experience_years`, `skills_count`, `certifications`): Standardized using `StandardScaler`.
- **Categorical Features** (`job_title`, `education_level`, `industry`, etc.): Encoded using `OneHotEncoder`.

### 2.2 Model Optimization (Grid Search)
To find the optimal configuration, we performed a Grid Search on a 20% random subsample (40,000 rows). We tested 8 combinations of:
- **Architectures**: `[128, 64]` vs `[256, 128, 64]`
- **Learning Rates**: `0.01` vs `0.001`
- **Dropout Rates**: `0.1` vs `0.3`

**Winning Configuration**:
- **Layers**: 256 -> 128 -> 64
- **Learning Rate**: 0.01
- **Dropout**: 0.1

## 3. Results

### 3.1 Model Performance
The final model, trained on the full dataset for 50 epochs, yielded the following metrics on the held-out test set (20%):
- **Mean Absolute Error (MAE)**: **$4,772.83**
- **R-squared (R2)**: **0.9745**

### 3.2 Key Insights
- **Experience vs. Salary**: A strong linear correlation exists, but education level and specific high-demand industries (like AI Engineering and Data Science) provide significant nonlinear premiums.
- **Model Accuracy**: The high R2 score indicates that the features provided (Experience, Education, Industry) are extremely strong predictors of salary, with very little unexplained variance.

## 4. Conclusion
The implementation of a Deep Neural Network proved highly effective for this tabular dataset. The Two-Phase training approach allowed for rigorous hyperparameter tuning without exceeding the computational limits of a personal computer.
