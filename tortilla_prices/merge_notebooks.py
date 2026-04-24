import json
import os

notebooks = [
    'explore_data.ipynb',
    'arima_forecast.ipynb',
    'wage_vs_tortilla.ipynb'
]

combined_cells = []
metadata = None
nbformat = None
nbformat_minor = None

for nb_file in notebooks:
    if os.path.exists(nb_file):
        with open(nb_file, 'r') as f:
            nb = json.load(f)
            # Add a separator
            combined_cells.append({
                "cell_type": "markdown",
                "metadata": {},
                "source": [f"---\n# Section from: {nb_file}\n---"]
            })
            combined_cells.extend(nb['cells'])
            if metadata is None:
                metadata = nb.get('metadata', {})
                nbformat = nb.get('nbformat', 4)
                nbformat_minor = nb.get('nbformat_minor', 4)

combined_nb = {
    "cells": combined_cells,
    "metadata": metadata,
    "nbformat": nbformat,
    "nbformat_minor": nbformat_minor
}

with open('tortilla_prices_analysis.ipynb', 'w') as f:
    json.dump(combined_nb, f, indent=1)

# Remove old notebooks
for nb_file in notebooks:
    if os.path.exists(nb_file):
        os.remove(nb_file)

print("Notebooks combined successfully into tortilla_prices_analysis.ipynb")
