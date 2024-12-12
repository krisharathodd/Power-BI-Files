#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix


# In[2]:


data = pd.read_csv(r'C:\Users\MITALI\Downloads\archive (13)\creditcard.csv')


# In[3]:


# Split the features and the target variable
X = data.drop(columns=['Amount', 'Class'])  # Features: all columns except 'Amount' and 'Class'
y = data['Class']  # Target: 'Class'


# In[4]:


# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)


# In[5]:


# Initialize the Random Forest classifier with pruning parameters
rf_model = RandomForestClassifier(
    n_estimators=100,          # Number of trees in the forest
    max_depth=10,              # Maximum depth of each tree (adjustable for pruning)
    min_samples_split=10,      # Minimum number of samples required to split an internal node
    min_samples_leaf=5,        # Minimum number of samples required to be at a leaf node
    random_state=42
)


# In[6]:


# Train the model
rf_model.fit(X_train, y_train)


# In[7]:


# Make predictions on the test set
y_pred = rf_model.predict(X_test)


# In[8]:


# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy}")
print("Classification Report:\n", classification_report(y_test, y_pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))

