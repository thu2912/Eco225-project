#!/usr/bin/env python
# coding: utf-8

# # Predict housing price in King County
# 
# **Project1 check list**:
# 
# 1. Introduction
# 2. Data Cleaning/Loading
# 3. Summary Statistics Tables
# 4. Plots, Histograms, Figures
# 5. Conclusion
# 
# **Resource/Idea**: 
# 
# - link:https://www.kaggle.com/code/chrisbronner/regression-r2-0-82-and-map-visualization/notebook
# 
# **Citation**: 

# 

# In[1]:


import pandas as pd


# In[2]:


data = pd.read_csv("kc_housing.csv")

df = pd.DataFrame(data)

df


# In[3]:


df2 = df[["price", "sqft_living", "grade", "sqft_lot", "view","yr_built"]]
df2


# In[49]:


df2["price"].plot.hist(bins=30, range=[0,6.450000e+05])
df2["price"].describe()


# In[28]:


df2["sqft_living"].describe()
df2["sqft_living"].plot.hist(bins=30, range=[290, 13540])


# In[43]:


df2["sqft_lot"].plot.hist(bins=30, range=[5.200000e+02, 1.068800e+05])
df2["sqft_lot"].describe()


# In[19]:


df2["view"].value_counts().sort_index().plot(xlabel = "Rating view", 
                                             ylabel = "Frequency",
                                             kind="bar")  # bar plot of view rating and frequency


# In[42]:


df2["grade"].value_counts().sort_index().plot(xlabel = "Grade", 
                                             ylabel = "Frequency",
                                             kind="bar") 


# In[44]:


df2["yr_built"].plot.hist(bins=30)


# In[5]:


sp1 =  df2.plot.scatter(x='sqft_living',
                      y='price') # relation of price and sft living


# In[8]:


sp2 =  df2.plot.scatter(x='yr_built',
                      y='price') # relation of year built and house price


# In[50]:


sp3 =  df2.plot.scatter(x='grade',
                      y='price')


# In[51]:


sp4 =  df2.plot.scatter(x='view',
                      y='price')


# In[ ]:




