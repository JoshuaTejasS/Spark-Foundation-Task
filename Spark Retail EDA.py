#!/usr/bin/env python
# coding: utf-8

# In[41]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# In[4]:


data = pd.read_csv("C:/Users/joshh/Downloads/SampleSuperstore.csv")


# In[5]:


data.head()


# In[6]:


data.tail()


# In[7]:


data.describe()


# In[8]:


data.nunique()


# In[9]:


data.shape


# In[10]:


data.columns


# In[11]:


data.isnull()


# In[12]:


data.isnull().sum()


# In[13]:


store = data.drop(['Postal Code'], axis=1)


# In[14]:


store.head()


# In[15]:


store.describe()


# In[16]:


correlation = store.corr()


# In[17]:


correlation


# In[18]:


covariance = store.cov()


# In[19]:


covariance


# In[20]:


sns.heatmap(correlation, xticklabels=correlation.columns, yticklabels=correlation.columns, annot=True)


# In[21]:


store['State'].value_counts()


# In[22]:


plt.figure(figsize=(15,15))
sns.countplot(x=store['State'])
plt.xticks(rotation=90)
plt.title("States")
plt.show()


# In[23]:


sns.set(style="whitegrid")
plt.figure(2, figsize=(20,15))
sns.barplot(x='Sub-Category',y='Profit', data=store, palette='PuBuGn')
plt.suptitle('Profits on Each Category', fontsize=16)
plt.show()


# In[24]:


figsize=(15,10)
sns.pairplot(store,hue='Sub-Category')
plt.show()


# In[33]:


figsize=(15,10)
sns.pairplot(store,hue='Category')
plt.show()


# In[25]:


figsize=(15,10)
sns.pairplot(store,hue='Segment')
plt.show()


# In[39]:


figsize=(15,10)
sns.pairplot(store,hue='Region')
plt.show()


# In[46]:


store['Region'].value_counts()


# In[36]:


plt.pie(store['Region'].value_counts(),labels=["West","East","Central","South"])
plt.show()


# In[31]:


plt.figure(figsize=(10,4))
sns.lineplot(x='Discount',y='Sales', data=store , color='b',label='Discount vs Sales')
plt.legend()
plt.show()


# In[33]:


plt.figure(figsize=(10,4))
sns.lineplot(x='Discount',y='Profit', data=store , color='g',label='Discount vs Profit')
plt.legend()
plt.show()

