# Omnichannel Equilibrium: Causal MARL for Dynamic Pricing

This repository contains the implementation of **"The Omnichannel Equilibrium"**, a prescriptive analytics system that combines Double Machine Learning (DML) for Causal Inference and Multi-Agent Reinforcement Learning (MARL) to optimize global dynamic pricing and inventory allocation.

## Contents
- `data/`: Contains the datasets used for this project (e.g., shoe sales dataset).
- `explore_data.ipynb`: Initial exploratory data analysis (EDA) of the global shoe sales dataset.
- `omnichannel_equilibrium.ipynb`: The core notebook containing the architecture, the Causal ML setup, the world simulator, and the MARL agent simulation.
- `run_experiment.py`: The python script used to run the end-to-end test and generate plots.
- `REPORT.md`: A deep-dive research report on the methodology, architecture, and simulation results.

## Quick Start
1. Install dependencies:
   ```bash
   pip install torch econml scikit-learn ray[rllib] gym pandas numpy matplotlib seaborn
   ```
2. Open `omnichannel_equilibrium.ipynb` and run the simulation cells to observe the dynamic pricing agent in action.

## Highlights
- **Double Machine Learning**: Used to isolate the conditional average treatment effect (CATE) of price changes on demand.
- **Entity Embeddings**: Handles high-cardinality categorical features (e.g., Brand, Color).
- **Hype Index**: A custom momentum metric used to provide time-series awareness to the agent.
- **MARL Simulator**: A custom `MarketWorldModel` that simulates realistic market dynamics for RL agents to interact with.
