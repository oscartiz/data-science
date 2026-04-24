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

# Filter for Sonora
sonora_df = df[df['State'] == 'Sonora'].copy()

# Segment cities
border_cities = ['Nogales', 'San Luis Río Colorado']
# The data has 'San Luis Río Colorado'? The unique check showed: 'Nogales', 'San Luis Río Colorado', 'Cd. Obregón', 'Hermosillo'.
# But wait, looking at the previous output, it was 'San\xa0Luis\xa0Río\xa0Colorado' (non-breaking spaces). I'll use string contains to be safe.
sonora_df['Zone'] = sonora_df['City'].apply(lambda x: 'Border (ZLFN)' if 'Nogales' in x or 'San' in x else 'Non-Border (SMG)')

# Aggregate average price by year and zone
yearly_price_zone = sonora_df.groupby(['Year', 'Zone'])['Price per kilogram'].mean().reset_index()

# Historical Minimum Wage (2007-2024)
wage_data = {
    'Year': [2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024],
    'SMG_Wage': [50.57, 52.59, 54.80, 57.46, 59.82, 62.33, 64.76, 67.29, 70.10, 73.04, 80.04, 88.36, 102.68, 123.22, 141.70, 172.87, 207.44, 248.93],
    'ZLFN_Wage': [50.57, 52.59, 54.80, 57.46, 59.82, 62.33, 64.76, 67.29, 70.10, 73.04, 80.04, 88.36, 176.72, 185.56, 213.39, 260.34, 312.41, 374.89]
}
df_wage = pd.DataFrame(wage_data)

# Calculate Growth Index
base_smg = df_wage.loc[df_wage['Year'] == 2007, 'SMG_Wage'].values[0]
df_wage['SMG Growth Index'] = (df_wage['SMG_Wage'] / base_smg) * 100

# Plotting
sns.set_theme(style="whitegrid")
fig, axes = plt.subplots(1, 2, figsize=(18, 6), sharey=False)

# Subplot 1: Non-Border (Hermosillo, Obregón)
non_border = yearly_price_zone[yearly_price_zone['Zone'] == 'Non-Border (SMG)'].copy()
base_price_nb = non_border.loc[non_border['Year'] == 2007, 'Price per kilogram'].values[0]
non_border['Price Growth Index'] = (non_border['Price per kilogram'] / base_price_nb) * 100

merged_nb = pd.merge(non_border, df_wage, on='Year')

axes[0].plot(merged_nb['Year'], merged_nb['Price Growth Index'], marker='o', label='Tortilla Price Growth', color='red', linewidth=2)
axes[0].plot(merged_nb['Year'], merged_nb['SMG Growth Index'], marker='s', label='Standard Min Wage Growth', color='green', linewidth=2)
axes[0].axhline(100, color='grey', linestyle='--', alpha=0.6)
axes[0].set_title('Non-Border Sonora (Hermosillo, Cd. Obregón)', fontsize=14)
axes[0].set_xlabel('Year', fontsize=12)
axes[0].set_ylabel('Growth Index (2007 = 100)', fontsize=12)
axes[0].legend()

final_nb = merged_nb.iloc[-1]
axes[0].annotate(f"{final_nb['Price Growth Index']:.1f}%", (final_nb['Year'], final_nb['Price Growth Index']), textcoords="offset points", xytext=(0,10), ha='center', color='red', fontweight='bold')
axes[0].annotate(f"{final_nb['SMG Growth Index']:.1f}%", (final_nb['Year'], final_nb['SMG Growth Index']), textcoords="offset points", xytext=(0,-15), ha='center', color='green', fontweight='bold')

# Subplot 2: Border (Nogales, San Luis)
border = yearly_price_zone[yearly_price_zone['Zone'] == 'Border (ZLFN)'].copy()
base_year_border = border['Year'].min()
base_price_b = border.loc[border['Year'] == base_year_border, 'Price per kilogram'].values[0]
border['Price Growth Index'] = (border['Price per kilogram'] / base_price_b) * 100

base_wage_b = df_wage.loc[df_wage['Year'] == base_year_border, 'ZLFN_Wage'].values[0]
df_wage['ZLFN Growth Index'] = (df_wage['ZLFN_Wage'] / base_wage_b) * 100

merged_b = pd.merge(border, df_wage, on='Year')

axes[1].plot(merged_b['Year'], merged_b['Price Growth Index'], marker='o', label=f'Tortilla Price Growth (Base={base_year_border})', color='red', linewidth=2)
axes[1].plot(merged_b['Year'], merged_b['ZLFN Growth Index'], marker='s', label=f'ZLFN Min Wage Growth (Base={base_year_border})', color='blue', linewidth=2)
axes[1].axhline(100, color='grey', linestyle='--', alpha=0.6)
axes[1].set_title('Border Sonora (Nogales, San Luis Río Colorado)', fontsize=14)
axes[1].set_xlabel('Year', fontsize=12)
axes[1].legend()

final_b = merged_b.iloc[-1]
axes[1].annotate(f"{final_b['Price Growth Index']:.1f}%", (final_b['Year'], final_b['Price Growth Index']), textcoords="offset points", xytext=(0,10), ha='center', color='red', fontweight='bold')
axes[1].annotate(f"{final_b['ZLFN Growth Index']:.1f}%", (final_b['Year'], final_b['ZLFN Growth Index']), textcoords="offset points", xytext=(0,-15), ha='center', color='blue', fontweight='bold')

plt.suptitle('The Two Sonoras: Purchasing Power Divergence (Tortilla Prices vs. Minimum Wage)', fontsize=18)
plt.tight_layout()

output_path = '/Users/tiz/.gemini/antigravity/brain/b62d5b93-c0e4-4ddd-9305-f182f234878e/sonora_divergence.png'
plt.savefig(output_path, dpi=300, bbox_inches='tight')
print(f"Plot saved to {output_path}")
