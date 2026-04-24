import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.ensemble import RandomForestRegressor
from econml.dml import LinearDML
from sklearn.preprocessing import LabelEncoder
import warnings
warnings.filterwarnings('ignore')

# 1. Load data
print("Loading data...")
df = pd.read_csv('data/shoes_sales_dataset.csv')
df['Date'] = pd.to_datetime(df['Date'])
df = df.sort_values('Date')

# 2. Feature Engineering
le_brand = LabelEncoder()
df['Brand_Idx'] = le_brand.fit_transform(df['Brand'])
le_channel = LabelEncoder()
df['Channel_Idx'] = le_channel.fit_transform(df['Sales_Channel'])

# Hype Index calculation
df['Hype_Index'] = df['Units_Sold'].ewm(span=7).mean() / (df['Units_Sold'].ewm(span=30).mean() + 1e-5)

X = df[['Hype_Index', 'Brand_Idx', 'Channel_Idx']].fillna(0).values
T = df['Price_USD'].values
Y = df['Units_Sold'].values

# 3. Causal Inference
print("Training Causal Model (Double ML)...")
dml = LinearDML(
    model_y=RandomForestRegressor(n_estimators=20, max_depth=5, random_state=42),
    model_t=RandomForestRegressor(n_estimators=20, max_depth=5, random_state=42),
    discrete_treatment=False,
    cv=2
)
dml.fit(Y, T, X=X)
print("Causal Model trained.")

baseline_demand_model = RandomForestRegressor(n_estimators=20, max_depth=5, random_state=42)
baseline_demand_model.fit(X, Y)

# 4. Market Simulator Setup
class MarketWorldModel:
    def __init__(self, causal_model, baseline_demand_model):
        self.causal_model = causal_model
        self.baseline_demand = baseline_demand_model
        
    def simulate_demand(self, state_features, action_price_adjustment):
        base_demand = self.baseline_demand.predict(state_features)
        elasticity = self.causal_model.effect(state_features)
        noise = np.random.normal(0, 0.05 * base_demand)
        # Price adjustment is a fraction (e.g. 0.1 for 10% increase)
        # Demand = Base + (Elasticity * delta_price) + noise
        # Note: elasticity is d(Units)/d(Price). delta_price = base_price * action_price_adjustment
        # For simplicity, we assume a base price of 120.
        delta_price = 120.0 * action_price_adjustment
        simulated_demand = base_demand + (elasticity * delta_price) + noise
        return np.maximum(0, simulated_demand)

world_model = MarketWorldModel(dml, baseline_demand_model)

# 5. Simulation Loop
days = 60
inventory = 1000
base_price = 120.0

inventories = []
revenues = []
demands = []
prices = []

state = np.array([[1.0, 0, 0]]) # Example: Hype=1.0, Brand=0, Channel=0

for day in range(days):
    # Dynamic Pricing Agent Heuristic
    if inventory > 800:
        price_adj = -0.15 # 15% discount
    elif inventory > 400:
        price_adj = 0.00  # Baseline
    elif inventory > 150:
        price_adj = 0.15  # 15% premium
    else:
        price_adj = 0.30  # 30% premium
        
    actual_price = base_price * (1 + price_adj)
    
    # Simulate market response
    demand = world_model.simulate_demand(state, price_adj)[0]
    sold = min(demand, inventory)
    inventory -= sold
    
    revenue = sold * actual_price
    
    inventories.append(inventory)
    revenues.append(revenue)
    demands.append(demand)
    prices.append(actual_price)
    
    # State transition (random walk for hype)
    state[0][0] = max(0.5, min(2.0, state[0][0] + np.random.normal(0, 0.05)))
    
    # Restock schedule
    if day % 14 == 0 and day > 0:
        inventory += 400

# 6. Plotting
sns.set_theme(style="whitegrid")
fig, axs = plt.subplots(2, 2, figsize=(14, 10))

axs[0, 0].plot(inventories, color='blue', linewidth=2)
axs[0, 0].set_title('Inventory Level Over Time', fontsize=14)
axs[0, 0].set_ylabel('Units in Stock')
axs[0, 0].set_xlabel('Days')
# Add restock lines
for x in range(14, days, 14):
    axs[0, 0].axvline(x=x, color='gray', linestyle='--', alpha=0.5)

axs[0, 1].step(range(days), prices, color='green', linewidth=2, where='mid')
axs[0, 1].set_title('Dynamic Pricing Actions', fontsize=14)
axs[0, 1].set_ylabel('Price (USD)')
axs[0, 1].set_xlabel('Days')

axs[1, 0].plot(demands, color='orange', linewidth=2)
axs[1, 0].set_title('Simulated Daily Demand', fontsize=14)
axs[1, 0].set_ylabel('Units Demanded')
axs[1, 0].set_xlabel('Days')

cumulative_revenue = np.cumsum(revenues)
axs[1, 1].plot(cumulative_revenue, color='purple', linewidth=2)
axs[1, 1].fill_between(range(days), cumulative_revenue, color='purple', alpha=0.1)
axs[1, 1].set_title('Cumulative Revenue', fontsize=14)
axs[1, 1].set_ylabel('Revenue (USD)')
axs[1, 1].set_xlabel('Days')

plt.tight_layout()
output_path = '/Users/tiz/.gemini/antigravity/brain/b62d5b93-c0e4-4ddd-9305-f182f234878e/omnichannel_simulation.png'
plt.savefig(output_path, dpi=300, bbox_inches='tight')
print(f"Plot saved to {output_path}")

