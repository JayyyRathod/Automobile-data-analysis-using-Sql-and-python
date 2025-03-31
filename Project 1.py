#!/usr/bin/env python
# coding: utf-8

# In[24]:


import pyodbc
import pandas as pd


conn = pyodbc.connect(
    'DRIVER={SQL Server};'
    'SERVER=Jayesh\\SQLEXPRESS;'
    'DATABASE=Automobile;'
    'Trusted_Connection=yes;'
)



# In[28]:


Automobile_data_mileage_df=pd.read_sql("select * from Automobile_data_mileage",conn)


# In[30]:


Automobile_data_mileage_df


# In[44]:


Automobile_data_mileage_df.head()


# In[46]:


Automobile_data_mileage_df.tail()


# In[36]:


Automobile_data_price_df=pd.read_sql("select * from Automobile_data_price",conn)


# In[38]:


Automobile_data_price_df


# In[48]:


Automobile_data_price_df.tail()


# In[50]:


Automobile_data_price_df.head()


# In[54]:


import pandas as pd
import requests
from io import StringIO

# Fetch data from URLs
mileage_url = "https://hebbkx1anhila5yf.public.blob.vercel-storage.com/Automobile_data_mileage-duXfofV9dS5Ym1AL2NNgFzIFvBIWiP.csv"
price_url = "https://hebbkx1anhila5yf.public.blob.vercel-storage.com/Automobile_data_price-oMLmlhjANohMSjiqvknfnR2SbOMilU.csv"

mileage_response = requests.get(mileage_url)
price_response = requests.get(price_url)

mileage_df = pd.read_csv(StringIO(mileage_response.text))
price_df = pd.read_csv(StringIO(price_response.text))

#  Que 1 : Create a Dataframes of Toyota and Volkswagon for price and mileage

toyota_price = price_df[price_df['company'] == 'toyota'][['company', 'price']]
volkswagen_price = price_df[price_df['company'] == 'volkswagen'][['company', 'price']]
toyota_mileage = mileage_df[mileage_df['company'] == 'toyota'][['company', 'average-mileage']]
volkswagen_mileage = mileage_df[mileage_df['company'] == 'volkswagen'][['company', 'average-mileage']]

print("Toyota Price DataFrame:")
print(toyota_price)
print("\nVolkswagen Price DataFrame:")
print(volkswagen_price)
print("\nToyota Mileage DataFrame:")
print(toyota_mileage)
print("\nVolkswagen Mileage DataFrame:")
print(volkswagen_mileage)


# In[56]:


# Que 2 : print th statistics of only Volvo models

volvo_stats = mileage_df[mileage_df['company'] == 'volvo'].describe()
print("\nVolvo Models Statistics:")
print(volvo_stats)



# In[58]:


# • Que 3 : Remove column num of cylinders in mileage dataframe 1

mileage_df_no_cylinders = mileage_df.drop('num-of-cylinders', axis=1)
print("\nMileage DataFrame without num-of-cylinders column:")
print(mileage_df_no_cylinders.head())



# In[60]:


# Que 4: Give Horsepower details of audi models

audi_horsepower = mileage_df[mileage_df['company'] == 'audi'][['ID', 'company', 'horsepower']]
print("\nAudi Models Horsepower Details:")
print(audi_horsepower)



# In[62]:


# Que 5 : Change the Datatype of length column to integer in Mileage Dataframe

mileage_df['length'] = mileage_df['length'].astype(int)
print("\nMileage DataFrame with length column as integer:")
print(mileage_df[['ID', 'company', 'length']].head())
print(mileage_df['length'].dtype)


# In[ ]:




