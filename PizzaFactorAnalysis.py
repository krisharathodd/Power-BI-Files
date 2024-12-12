#!/usr/bin/env python
# coding: utf-8

# In[2]:


from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import FactorAnalysis
import pandas as pd

# Load your dataset (replace 'file_path' with the actual path if needed)
file_path = 'Pizza.csv'
data = pd.read_csv(file_path)

# Selecting relevant columns for factor analysis
features = ['mois', 'prot', 'fat', 'ash', 'sodium', 'carb', 'cal']

# Standardize the data
scaler = StandardScaler()
data_standardized = scaler.fit_transform(data[features])

# Perform Factor Analysis with 2 factors (adjust the number of factors if needed)
factor = FactorAnalysis(n_components=2, random_state=0)
factor_results = factor.fit_transform(data_standardized)

# Get factor loadings
factor_loadings = pd.DataFrame(factor.components_, columns=features)

# Get factor scores (transformed data)
factor_scores = pd.DataFrame(factor_results, columns=['Factor1', 'Factor2'])

# Display results
print("Factor Loadings:\n", factor_loadings)
print("\nFactor Scores:\n", factor_scores.head())


# In[ ]:




