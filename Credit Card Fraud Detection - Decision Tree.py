#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


df = pd.read_csv(r'C:\Users\MITALI\Downloads\archive (13)\creditcard.csv')


# In[3]:


df.columns


# In[4]:


df.head(3)


# In[5]:


df.info()


# In[6]:


df.describe()


# In[7]:


df.isnull().sum()


# In[ ]:


sns.pairplot(df,hue='Class',palette='Set1')


# ## Train Test and Split

# In[8]:


from sklearn.model_selection import train_test_split


# In[9]:


X = df.drop('Class',axis=1)
y = df['Class']


# In[10]:


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30)


# In[ ]:





# ## Decision Tress

# In[11]:


from sklearn.tree import DecisionTreeClassifier


# In[12]:


dtree = DecisionTreeClassifier(criterion='entropy', random_state=0)


# In[13]:


dtree.fit(X_train,y_train)


# ## Prediction and Evaluation

# In[14]:


predictions = dtree.predict(X_test)


# In[15]:


predictions


# In[16]:


from sklearn.metrics import classification_report,confusion_matrix


# In[17]:


print(classification_report(y_test,predictions))


# In[18]:


print(confusion_matrix(y_test,predictions))


# In[22]:


plt.figure(figsize=(20, 25))
tree.plot_tree(
    dtree,
    feature_names=feature_names,  # Use the list of feature names
    class_names=['Class-1', 'Class-0'],
    rounded=True,  # Rounded node edges
    filled=True,  # Adds color according to class
    proportion=True
)
plt.show()


# In[ ]:




