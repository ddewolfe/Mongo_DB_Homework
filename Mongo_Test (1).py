
# coding: utf-8

# In[ ]:


# Dylan DeWolfe
# CPSC 408 
# Mongo Homework


# In[6]:


import pymongo
from pymongo import MongoClient


# In[9]:


client = pymongo.MongoClient("mongodb+srv://ddewolfe:2421@cluster0-mmntd.gcp.mongodb.net/test?retryWrites=true&w=majority")
db = client['mongo_test']


# In[13]:



db.hw1.insert_one({"Pizza_size": "12 inch", "Topping 1":"Pepperoni","Topping2":'Sausage', "Topping3":"Bacon"})

# # select document 
for s in db.hw1.find():
print(s) 

