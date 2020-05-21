#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy as sp
import lxml.html as lx
import requests
import requests_cache
requests_cache.install_cache("../sfchronicle")
import time
import re
import nltk
import nltk.corpus
nltk.download('stopwords')
from itertools import chain
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[ ]:


from bs4 import BeautifulSoup
html_soup = BeautifulSoup(response.text, 'html.parser')
type(html_soup)


# ## Step One: Get the links of 500 articles

# In[ ]:


def get_links_one_page(url):
    
    # Load in the web page 
    response = requests.get(url)
    html_soup = BeautifulSoup(response.text, 'html.parser')
    
    
    # Get all the articles on that page
    articles = html_soup.find_all('div', class_ = 'col-md-4 col-sm-6 spacer-xs')
    
    # Get the text form 
    all_text = [str(articles[i].a) for i in range(0,len(articles))]
    
    # Get the links
    links = [re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', all_text[i])[0]
      for i in range(0,len(all_text))]
    
    return links


# #### Get links of all the different pages to scrape

# In[ ]:


months = [str(i) for i in range(1,10)]


# In[ ]:


# Will get all pages from janurary to october
all_pages = ["https://thatgrapejuice.net/2019/" + months[i] + "/page/" for i in range(0, len(months))]


# In[ ]:


all_pages


# In[ ]:


# Only want the first 5 pages of each month
pages = [str(i) for i in range(1,6)]


# In[ ]:


newl = []


# In[ ]:


# Gets the link for the first 5 pages for each month 
for i in range(0,len(all_pages)):
    for j in range(0,len(pages)):
                 newl.append(all_pages[i] + pages[j])


# In[ ]:


newl


# In[ ]:


# 50 urls, each urls has about 10-12 articles so 50 * 10 = i should get the links of 500 articles
len(newl)


# In[ ]:


# Scrape each of the 50 webpages to only get links of the articles 
all_article_urls = [get_links_one_page(newl[i]) for i in range(0, len(newl))]


# In[ ]:


# Since lenth is 50 that means our list is a nested list 
len(all_article_urls)


# In[ ]:


# Flatten nested list 
all_article_urls = sum(all_article_urls, [])


# In[ ]:


len(all_article_urls)


# ### Scrape each of the 500 webpages and store them as a json file 

# In[ ]:


def get_file_content(url):
    response = requests.get(url)
    return response.text


# In[ ]:


all_content = [get_file_content(all_article_urls[i]) for i in range(0,len(all_article_urls))]


# In[ ]:


bs(all_content)


# Can be used to get json files
# 
# for i in range(0, len(all_content)):
#     filename = str(subset[i]) + ".json"
#     with open(filename, 'w') as json_file:
#         json.dump(file_content, json_file)

# In[ ]:


len(all_content)


# In[ ]:


dat = {'Url': all_article_urls, 'Content': all_content}


# In[ ]:


final_df = pd.DataFrame(dat)


# In[ ]:


export = final_df.to_csv("articl_dat.csv", header = None, index = False)


# In[ ]:


final_df[0:5]


# In[ ]:


final_df.to_excel("final_df.xlsx")


# In[ ]:


write.csv(final_df)


# In[ ]:


final_df.to_csv('file.csv',encoding='utf-8-sig')


# In[ ]:


final_df["Url"][1]


# In[ ]:


x = all_content[2]


# In[ ]:


import re


# In[ ]:


result = re.findall('<p style="text-align: justify;">(.*)</p>',x )


# In[ ]:


len(result)


# In[ ]:


del result[-1]


# In[ ]:


len(result)


# In[ ]:


del result[0]


# In[ ]:


lol = "".join(result)


# In[ ]:


lol


# In[ ]:


def get_clean_content(txt):
    result = re.findall('<p style="text-align: justify;">(.*)</p>',txt)
    x = len(result) - 1
    final = "".join(result[:-1])
    return final


# In[ ]:


get_clean_content(all_content[1])


# In[ ]:


cleaned_text = [get_clean_content(all_content[i]) for i in range(0, len(all_content))]


# In[ ]:


final_df["cleaned_text"] = cleaned_text


# In[ ]:


final_df


# In[ ]:


final_df['Url'][538]


# In[ ]:




