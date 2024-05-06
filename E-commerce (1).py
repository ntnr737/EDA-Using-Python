#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib as mlt
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")


# In[2]:


df=pd.read_csv("D:\Project\Fashion-Ecommerce\FashionDataset\FD.csv")


# In[3]:


df


# In[4]:


df.drop(columns=["Unnamed: 0"], inplace=True)


# In[5]:


df


# In[6]:


df.head()


# In[7]:


df.shape


# In[8]:


df.isnull().sum()


# In[9]:


df.info()


# In[10]:


df.nunique()


# In[11]:


df.replace("Nan", np.nan, inplace=True)


# In[12]:


df.dropna(axis=0,inplace=True)


# In[13]:


df.shape


# In[14]:


df.head()


# In[15]:


df["MRP"]=df["MRP"].str.replace("Rs\n","")


# In[16]:


df["MRP"].info()


# In[17]:


df["MRP"]=df["MRP"].astype(int)


# In[18]:


df["MRP"].info()


# In[19]:


df["SellPrice"]=df["SellPrice"].astype(int)


# In[20]:


df.info()


# In[21]:


df


# In[22]:


df["Discount"]=df["Discount"].str.replace("% off","")


# In[23]:


df


# In[24]:


df["Discount"]=df["Discount"].astype(int)


# In[25]:


df.info()


# In[26]:


df["Category"]=df["Category"].str.replace("-Women","")


# In[27]:


df["Category"]


# In[28]:


df


# In[29]:


df["Sizes"]=df["Sizes"].str.replace("Size:","")


# In[30]:


df


# In[31]:


df=df[df["Sizes"] != "Error Size"]


# In[32]:


df


# In[33]:


df.describe()


# In[34]:


df.columns


# In[35]:


df.rename(columns={"Discount" : 'Discount_%'}, inplace=True)


# In[36]:


df


# In[37]:


df["Discount_%"].unique()


# In[38]:


def discount_range(i):
    if i in range(0,26):
        return str("0-25%")
    if i in range(26,51):
        return str("26-50%")
    elif i in range(51,76):
        return str("51-75%")
    else:
        return str(">75%")


# In[39]:


df["Discount_range"]=df["Discount_%"].apply(discount_range)


# In[40]:


df["Discount_range"].unique()


# In[41]:


df


# In[42]:


df["Discount_range"].value_counts()


# In[149]:


plt.figure(figsize=(8, 4))  # Set the figure size
sns.color_palette("viridis")  # Using a colorful palette

df["Discount_range"].value_counts().plot.bar(fontsize=12, edgecolor='black')  # Plotting the bar chart
plt.xticks(rotation=0, fontsize=10)
plt.xlabel("Discount by Range", fontsize=10)
plt.ylabel("Sales", fontsize=10)
plt.title("Counts by Discounts", fontsize=12)
plt.tight_layout()
plt.show()


# In[44]:


df.columns


# In[45]:


df["Category"].unique()


# In[47]:


Category_fashion=df[df["Category"]== "Westernwear"]


# In[48]:


Category_fashion


# In[51]:


Category_indianwear=df[df["Category"]== "Indianwear"]


# In[52]:


Category_indianwear


# In[53]:


Category_lnightwear=df[df["Category"]== "Lingerie&Nightwear"]


# In[54]:


Category_lnightwear


# In[58]:


Category_footwear=df[df["Category"]== "Footwear"]


# In[59]:


Category_footwear


# In[61]:


Category_footwear["Discount_range"].value_counts()


# In[62]:


def selling_range(i):
    if i in range (0,1501):
        return str("0-1500")
    if i in range (1501,3501):
        return str("1500-3500")
    elif i in range (3501,5501):
        return str("3500-5500")
    else:
        return str(">5500")


# In[63]:


df["Sell_range"]=df["SellPrice"].apply(selling_range)


# In[64]:


df


# In[66]:


df["Sell_range"].value_counts()


# In[145]:


plt.figure(figsize=(10, 6))  # Set the figure size
colors = sns.color_palette("viridis", len(df["Sell_range"].unique()))  # Using a colorful palette
sns.set_palette(colors)  # Set the palette for seaborn
df["Sell_range"].value_counts().plot.bar(fontsize=12, edgecolor='black')
plt.xticks(rotation=0, fontsize=10)
plt.yticks(fontsize=10)
plt.xlabel("Sell by Range", fontsize=12)
plt.ylabel("Sell by Price", fontsize=12)
plt.title("Counts by Discounts", fontsize=14)
plt.tight_layout()
plt.show()


# In[70]:


Category_fashion_range=df[df["Category"]== "Westernwear"]


# In[79]:


Category_fashion_range["SellPrice"].value_counts()


# In[153]:


plt.figure(figsize=(10, 6))  # Increased the figure size for better readability
sns.barplot(data=df, x="Category", y="SellPrice", palette="viridis")  # Used a colorful palette
plt.xticks(rotation=0, fontsize=10)
plt.yticks(fontsize=10)
plt.xlabel("Category", fontsize=12)
plt.ylabel("Sell by Price", fontsize=12)
plt.title("Sales", fontsize=14)
plt.tight_layout()
plt.show()


# In[ ]:





# In[130]:


df["Category"].unique()


# In[160]:


fashion_footwear=df[df["Category"]=="Footwear"]


# In[156]:


df.columns


# In[157]:


plt.figure(figsize=(8, 5))  # Set the figure size
sns.countplot(data=fashion_footwear, x="Sell_range", palette="Set2")  # Using countplot with a colorful palette
plt.xlabel("Sell Range", fontsize=12)  # X-axis label with adjusted font size
plt.ylabel("Count", fontsize=12)  # Y-axis label with adjusted font size
plt.title("Counts by Sell Range", fontsize=14)  # Title with adjusted font size
plt.xticks(rotation=0, fontsize=10)  # Rotate x-axis labels and adjust font size
plt.yticks(fontsize=10)  # Adjust font size of y-axis ticks
plt.tight_layout()  # Adjust layout to prevent overlapping labels
plt.show()


# In[169]:


fashion_westernwear=df[df["Category"]=="Westernwear"]


# In[166]:


plt.figure(figsize=(8, 5))  # Set the figure size
sns.countplot(data=fashion_westernwear, x="Sell_range", palette="Set2")  # Using countplot with a colorful palette
plt.xlabel("Sell Range", fontsize=12)  # X-axis label with adjusted font size
plt.ylabel("Count", fontsize=12)  # Y-axis label with adjusted font size
plt.title("Counts by Sell Range Westernwear", fontsize=14)  # Title with adjusted font size
plt.xticks(rotation=0, fontsize=10)  # Rotate x-axis labels and adjust font size
plt.yticks(fontsize=10)  # Adjust font size of y-axis ticks
plt.tight_layout()  # Adjust layout to prevent overlapping labels
plt.show()


# In[168]:


fashion_indianwear=df[df["Category"]=="Indianwear"]


# In[171]:


plt.figure(figsize=(8, 5))  # Set the figure size
sns.countplot(data=fashion_indianwear, x="Sell_range", palette="Set2")  # Using countplot with a colorful palette
plt.xlabel("Sell Range", fontsize=12)  # X-axis label with adjusted font size
plt.ylabel("Count", fontsize=12)  # Y-axis label with adjusted font size
plt.title("Counts by Sell Range Indianwear", fontsize=14)  # Title with adjusted font size
plt.xticks(rotation=0, fontsize=10)  # Rotate x-axis labels and adjust font size
plt.yticks(fontsize=10)  # Adjust font size of y-axis ticks
plt.tight_layout()  # Adjust layout to prevent overlapping labels
plt.show()


# In[ ]:





# In[93]:


fashion_footwear["BrandName"].unique()


# In[104]:


df["BrandName"].value_counts().head(20).plot.bar(fontsize=10)


# In[178]:


brand_name=["BrandName"]


# In[ ]:





# In[124]:


plt.figure(figsize= (20,8))
sns.jointplot(x = df["MRP"],y=df["SellPrice"],kind="scatter")


# In[108]:


plt.figure(figsize= (20,8))
sns.jointplot(x = df["MRP"],y=df["SellPrice"],kind="scatter", hue=df["Discount_range"])


# In[114]:


sns.barplot(x=df["Discount_range"], y=df["MRP"])


# In[116]:


#Higher the MRP higher the discount, a product with MRP 3000 and discount 30% or 25%.
#Consumers perceive a higher level of saving for a product when higher price discount is provided.
#This  perception plays a crucial role in price-discount vale relation.
#There is a linear relationship b/w selling price and MRP


# In[ ]:


#ntnr737@gmail.com


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




