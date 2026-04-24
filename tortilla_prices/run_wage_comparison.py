import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

print("Loading data...")
df = pd.read_csv('data/tortilla_prices.csv')

# Drop missing values
df = df.dropna(subset=['Price per kilogram'])

# Aggregate average national price by year
yearly_price = df.groupby('Year')['Price per kilogram'].mean().reset_index()

# Historical Minimum Wage in Mexico (2007-2024) in Pesos per day
wage_data = {
    'Year': [2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024],
    'Minimum Wage (MXN/day)': [50.57, 52.59, 54.80, 57.46, 59.82, 62.33, 64.76, 67.29, 70.10, 73.04, 80.04, 88.36, 102.68, 123.22, 141.70, 172.87, 207.44, 248.93]
}
df_wage = pd.DataFrame(wage_data)

# Merge datasets
merged = pd.merge(yearly_price, df_wage, on='Year', how='inner')

# Calculate Growth Index (Base Year 2007 = 100)
base_price = merged.loc[merged['Year'] == 2007, 'Price per kilogram'].values[0]
base_wage = merged.loc[merged['Year'] == 2007, 'Minimum Wage (MXN/day)'].values[0]

merged['Price Growth Index'] = (merged['Price per kilogram'] / base_price) * 100
merged['Wage Growth Index'] = (merged['Minimum Wage (MXN/day)'] / base_wage) * 100

# Plotting
sns.set_theme(style="whitegrid")
plt.figure(figsize=(12, 6))

plt.plot(merged['Year'], merged['Price Growth Index'], marker='o', label='Tortilla Price Growth', color='red', linewidth=2)
plt.plot(merged['Year'], merged['Wage Growth Index'], marker='s', label='Minimum Wage Growth', color='green', linewidth=2)

plt.axhline(100, color='grey', linestyle='--', alpha=0.6)

plt.title('Growth Comparison: Tortilla Prices vs Minimum Wage in Mexico (2007 = 100)', fontsize=16)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Growth Index (2007 = 100)', fontsize=12)
plt.xticks(merged['Year'], rotation=45)
plt.legend(loc='upper left', fontsize=12)

# Annotate final values to accentuate the difference
final_year = merged.iloc[-1]
plt.annotate(f"{final_year['Price Growth Index']:.1f}%", 
             (final_year['Year'], final_year['Price Growth Index']), 
             textcoords="offset points", xytext=(0,10), ha='center', color='red', fontweight='bold')

plt.annotate(f"{final_year['Wage Growth Index']:.1f}%", 
             (final_year['Year'], final_year['Wage Growth Index']), 
             textcoords="offset points", xytext=(0,-15), ha='center', color='green', fontweight='bold')

output_path = '/Users/tiz/.gemini/antigravity/brain/b62d5b93-c0e4-4ddd-9305-f182f234878e/wage_vs_tortilla.png'
plt.savefig(output_path, dpi=300, bbox_inches='tight')
print(f"Plot saved to {output_path}")
