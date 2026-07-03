# Data Science Projects

Monorepo of applied data-science and ML projects. Each subproject is self-contained, with its own README and a full write-up in `REPORT.md`.

## Projects

### [Omnichannel Equilibrium](./omnichannel_equilibrium/) — causal MARL for dynamic pricing

A prescriptive analytics system combining **Double Machine Learning** (isolating the causal effect of price changes on demand) with **Multi-Agent Reinforcement Learning** on a custom market simulator to optimize global dynamic pricing and inventory allocation. Entity embeddings handle high-cardinality categoricals; a custom "Hype Index" gives agents time-series awareness. → [Report](./omnichannel_equilibrium/REPORT.md)

### [Tortilla Prices](./tortilla_prices/) — ARIMA forecasting of Mexican tortilla prices

Multidimensional analysis of tortilla prices in Mexico (2007–2024): a custom "Tortilla Index", ARIMA forecasting, and a price-growth vs. minimum-wage comparison, plus a state-level deep dive on Sonora. → [Report](./tortilla_prices/REPORT.md) · [Sonora report](./tortilla_prices/REPORT_SONORA.md)

### [Job Salary Prediction](./job_salary_prediction/) — PyTorch DNN regression

A deep neural network predicting annual salary from 250,000 job records (experience, education, industry, company size, remote status, skills), with grid-searched architecture and scikit-learn preprocessing. → [Report](./job_salary_prediction/REPORT.md)

## Layout

```
omnichannel_equilibrium/   # DML + MARL pricing system (notebooks, simulator, run_experiment.py)
tortilla_prices/           # ARIMA analysis scripts, notebooks, reports
job_salary_prediction/     # PyTorch DNN notebook + report
```

## License

MIT
