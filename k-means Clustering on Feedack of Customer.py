#!/usr/bin/env python
# coding: utf-8

# ### Step 1:
# Load the dataset

# In[1]:


import warnings
warnings.filterwarnings("ignore")
import pandas as pd


# In[2]:


trip_advi_df = pd.read_csv(r"C:\Users\Hp\Desktop\Python Code\Clustering by Irfan\Feedback of Hotels _ Restaurant\tripadvisor_review.csv")
trip_advi_df


# In[4]:


trip_Final = trip_advi_df.copy()


# ####  Removing Unnecessary variable

# In[5]:


del trip_advi_df['User_ID']


# In[6]:


trip_advi_df.info()


# In[7]:


trip_advi_df.head()


# ### Step 2:
# Extract the measurements from the DataFrame using its .values attribute:

# In[8]:


samples = trip_advi_df.values # get all row and columne with header 
samples


# ### Step 3: Elbow Method 
# 1. Measure the quality of clusterings with different numbers of clusters using the inertia. 
# 
# 2. For each of the given values of k, perform the following steps:
# 3. Create a KMeans instance called model with k clusters.
# 4. Fit the model to the grain data samples.
# 5. Append the value of the inertia_ attribute of model to the list inertias.

# In[9]:


from sklearn.cluster import KMeans
from yellowbrick.cluster import KElbowVisualizer
km = KMeans(random_state=42)
visualizer = KElbowVisualizer(km, k=(1,10),timings=False)
visualizer.fit(samples)        # Fit the data to the visualizer
visualizer.show()


# # Model or Algorithm

# In[10]:


model2 = KMeans(n_clusters=3,max_iter=100,random_state=42)


# In[11]:


trip_Final['Cluster_Made'] = model2.fit_predict(samples)
trip_Final.head()


# In[12]:


trip_Final.Cluster_Made = trip_Final.Cluster_Made.replace([0,1,2],['First Group','Second Group','Third Group'])
trip_Final.head()


# ### Final Cluster Centorids 

# In[13]:


model2.cluster_centers_


# In[14]:


trip_Final.Cluster_Made.value_counts(ascending=False)


# # Business Submission

# In[15]:


Submission = trip_Final.loc[:,['User_ID','Cluster_Made']]
Submission


# In[16]:


Submission.to_excel(r"C:\Users\Hp\Desktop\Python Code\Clustering by Irfan\Feedback of Hotels _ RestaurantTrip_output.xlsx",index=False,sheet_name="Output") 


# # Finished
