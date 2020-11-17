#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('python --version')


# In[2]:


get_ipython().system('pip install pymongo[srv]')


# In[4]:


import pymongo
from pymongo import MongoClient


# In[5]:


pymongo.version


# In[18]:


client = pymongo.MongoClient("mongodb+srv://admin:Gorilaz0278@cluster0.qwrx8.gcp.mongodb.net/test")


# In[19]:


client.list_database_names()


# In[27]:


db = client.anatel


# In[31]:


db.minas.count_documents({})


# In[ ]:





# In[ ]:




