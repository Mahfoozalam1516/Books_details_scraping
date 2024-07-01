#!/usr/bin/env python
# coding: utf-8

# In[51]:


import requests
from bs4 import BeautifulSoup
from tqdm import tqdm
import pandas as pd

link = 'https://books.toscrape.com/catalogue/page-1.html'


# In[48]:


data = []

for i in tqdm(range (1, 51)) :
    link = 'https://books.toscrape.com/catalogue/page-' + str (i) + '.html'
    
    res = requests.get(link)
    soup = BeautifulSoup(res.text, 'html.parser')
    
    for sp in soup.find_all('li', class_ = 'col-xs-6 col-sm-4 col-md-3 col-lg-3' ):
    
        book_link = 'https://books.toscrape.com/catalogue/' + sp.find_all ('a')[-1].get('href')
        title_link = sp.find_all ('a')[-1].get('title')

        img_link = 'https://books.toscrape.com/' + sp.find ('img'). get('src') [3:]

        rating = sp.find('p'). get('class')[-1]

        price = sp.find('p', class_ = 'price_color').text[1:]

        stock = sp.find('p', class_ = 'instock availability'). text. strip()
    
        data.append([title, rating, price, stock, book_link, img_link])


# In[49]:


len(data)


# In[50]:


data[0]


# In[52]:


df = pd.DataFrame(data, columns = ['title', 'rating', 'price', 'stock', 'book_link', 'img_link'])


# In[53]:


df.head()


# In[54]:


df.to_csv ('books.csv', index = False)


# In[ ]:





# In[ ]:





# In[8]:


res = requests.get(link)
soup = BeautifulSoup(res.text, 'html.parser')


# In[38]:


data = []

for sp in soup.find_all('li', class_ = 'col-xs-6 col-sm-4 col-md-3 col-lg-3' ):
    
 #   print(sp)
    #print ('----')
    book_link = 'https://books.toscrape.com/catalogue/' + sp.find_all ('a')[-1].get('href')
    title_link = sp.find_all ('a')[-1].get('title')
    
    img_link = 'https://books.toscrape.com/' + sp.find ('img'). get('src') [3:]
    
    rating = sp.find('p'). get('class')[-1]
    
    price = sp.find('p', class_ = 'price_color').text[1:]
    
    stock = sp.find('p', class_ = 'instock availability'). text. strip()
    
    data.append([title, rating, price, stock, book_link, img_link])
    
    #print(title_link, "|" , book_link, "|" ,img_link, "|" ,rating, "|" , price, "|" ,stock )
  #  break


# In[39]:


data[0]


# In[ ]:





# In[ ]:





# In[ ]:




