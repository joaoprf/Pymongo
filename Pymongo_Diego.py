#!/usr/bin/env python
# coding: utf-8

# In[12]:


get_ipython().system('python --version')


# In[21]:


get_ipython().system('pip install pymongo[srv]')


# In[14]:


import pymongo
import numpy as np
from pymongo import MongoClient


# In[20]:


pymongo.version


# In[22]:


client = pymongo.MongoClient("mongodb+srv://admin:Gorilaz0278@cluster0.qwrx8.gcp.mongodb.net/test")


# In[23]:


client.list_database_names()


# In[24]:


db = client.anatel


# In[28]:


db.minas.count_documents({})


# In[27]:


list(db.minas.find().limit(5))


# In[29]:


list(db.list_collections())


# In[30]:


max = db.minas.aggregate([{"$group":{ "_id": {}, "max": {"$max": "$QtdeSolic"}}}])
valor = np.array(list(max))
max = valor[0]['max']

result = db.minas.aggregate([{"$match":{"QtdeSolic":{"$eq": max
}}}])

list(result)


# In[31]:


result = db.minas.aggregate([{"$group":{ "_id": {}, "min": {"$min": "$QtdeSolic"}}}])
valor = np.array(list(result))
valor_minimo = valor[0]['min']
print(valor_minimo)


# In[33]:


result = db.minas.aggregate([{"$match":{"QtdeSolic":{"$eq": valor_minimo
}}}])

list(result)


# In[34]:


tipo_valores = db.minas.distinct("Tipo")
list(tipo_valores)


# In[ ]:




