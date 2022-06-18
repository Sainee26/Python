#!/usr/bin/env python
# coding: utf-8

# # Basic sales tax is applicable at a rate of 10% on all goods, except books, food, and medical products that are exempt. Import duty is an additional sales tax applicable on all imported goods at a rate of 5%, with no exemptions. 
# 
# # When I purchase items I receive a receipt which lists the name of all the items and their price (including tax), finishing with the total cost of the items, and the total amounts of sales taxes paid. The rounding rules for sales tax are that for a tax rate of n%, a shelf price of p contains (np/100 rounded up to the nearest 0.05) amount of sales tax. 

# ## Task: Write an application in Python that prints out the receipt details for these shopping baskets. 

# ### a) Input 1:
# 
# #### 1 book at 12.49 
# 
# #### 1 music CD at 14.99
# 
# #### 1 chocolate bar at 0.85

# In[34]:


import numpy as np


# In[35]:


class Problem(object):
  def create_map(self,string):
    quantity=list()
    product=list()
    price=list()
    flag=0
    string=string.replace("\n"," ")
    string=string.split(" ")
    for val in string:
      if val.isdigit():
        quantity.append(val)
      elif type(val)==str and val!='at' and flag!=1:
        product.append(val)
      elif type(val)==str and val=='at' and flag!=1:
        flag=1
      elif flag==1:
        price.append(float(val))
        flag=0
    #price=float(price)
    return quantity,product,price


# In[36]:


class Questions(Problem):
  def __init__(self,string):
      super().__init__()
      self.quantity,self.product,self.price=self.create_map(string)
  def print(self):
    no_tax=['book','chocolates_bar','packed of headache pills','chocolate_bar']
    tax=0
    total_price=0
    for i in range(len(self.quantity)):
      #print(self.quantity[i],self.product[i],self.price[i])
      if self.product[i] in no_tax and 'imported' in self.product[i]:
        tax+=self.price[i]*0.5
        self.price[i]=np.round(self.price[i]+(self.price[i]*0.5),2)
      elif self.product[i] not in no_tax and 'imported' in self.product[i]:
        self.price[i]=np.round(self.price[i]+(self.price[i]*0.15),2)
      elif self.product[i] not in no_tax:
        self.price[i]=np.round(self.price[i]+(self.price[i]*0.10),2)
      total_price+=self.price[i]
      print('{} {}: {}'.format(self.quantity[i],self.product[i],self.price[i]))
    print('Sales Taxes: ',tax)
    print('Total: ',np.round(total_price,2))


# In[37]:


str1='1 book at 12.49\n1 music_CD at 14.99\n1 chocolate_bar at 0.85'
Question1 = Questions(str1)
Question1.print()


# ### Input 2:
# 
# #### 1 imported box of chocolates at 10.00 1 imported bottle of perfume at 47.50 

# In[38]:


str1='1 imported box of chocolates at 10.00\n1 imported bottle of perfume at 47.50'
Question1 = Questions(str1)
Question1.print()


# ### Input 3:
# 
# #### 1 imported bottle of perfume at 27.99 1 bottle of perfume at 18.99
# 
# #### 1 packet of headache pills at 9.75
# 
# #### 1 box of imported chocolates at 11.25 

# In[39]:


str1='1 imported bottle of perfume at 27.99\n1 bottle of perfume at 18.99\n1 packet of headache pills at 9.75\n1 box of imported chocolates at 11.25'
Question1 = Questions(str1)
Question1.print()


# In[ ]:




