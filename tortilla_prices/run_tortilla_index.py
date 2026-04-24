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
    'SMG_Wage': [50.57, 52.59, 54.80, 57.46, 59.82, 62.33, 64.76, 67.29, 70.10, 73.04, 80.04, 88.36, 102.68, 123.22, 141.70, 172.87, 207.44, 248.93]
}
df_wage = pd.DataFrame(wage_data)

# Merge datasets
merged = pd.merge(yearly_price, df_wage, on='Year', how='inner')

# Calculate the Tortilla Index (kg of tortillas per day of minimum wage)
merged['Tortilla Index (kg/day)'] = merged['SMG_Wage'] / merged['Price per kilogram']

# Plotting
sns.set_theme(style="whitegrid")
plt.figure(figsize=(12, 6))

plt.plot(merged['Year'], merged['Tortilla Index (kg/day)'], marker='o', label='National Tortilla Index', color='goldenrod', linewidth=3)

# Highlight the lowest point (the Lost Decade bottom)
min_idx = merged['Tortilla Index (kg/day)'].idxmin()
plt.scatter(merged.loc[min_idx, 'Year'], merged.loc[min_idx, 'Tortilla Index (kg/day)'], color='red', s=100, zorder=5, label=f"Lowest Purchasing Power ({merged.loc[min_idx, 'Year']})")

plt.title('The Tortilla Index: Kilograms of Tortilla per Minimum Wage (2007 - 2024)', fontsize=16)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Tortilla Index (kg)', fontsize=12)
plt.xticks(merged['Year'], rotation=45)
plt.legend(loc='upper left', fontsize=12)

# Annotate final values to accentuate the difference
final_year = merged.iloc[-1]
start_year = merged.iloc[0]
plt.annotate(f"{start_year['Tortilla Index (kg/day)']:.2f} kg", 
             (start_year['Year'], start_year['Tortilla Index (kg/day)']), 
             textcoords="offset points", xytext=(0,-15), ha='center', color='black', fontweight='bold')

plt.annotate(f"{final_year['Tortilla Index (kg/day)']:.2f} kg", 
             (final_year['Year'], final_year['Tortilla Index (kg/day)']), 
             textcoords="offset points", xytext=(0,10), ha='center', color='goldenrod', fontweight='bold')

output_path = '/Users/tiz/.gemini/antigravity/brain/b62d5b93-c0e4-4ddd-9305-f182f234878e/tortilla_index.png'
plt.savefig(output_path, dpi=300, bbox_inches='tight')
print(f"Plot saved to {output_path}")
