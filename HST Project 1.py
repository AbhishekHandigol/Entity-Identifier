#!/usr/bin/env python
# coding: utf-8

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

from bs4 import BeautifulSoup
html_soup = BeautifulSoup(response.text, 'html.parser')
type(html_soup)


# ## Step One: Get the links of 500 articles

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
months = [str(i) for i in range(1,10)]


# Will get all pages from janurary to october
all_pages = ["https://thatgrapejuice.net/2019/" + months[i] + "/page/" for i in range(0, len(months))]
all_pages


# Only want the first 5 pages of each month
pages = [str(i) for i in range(1,6)]
newl = []


# Gets the link for the first 5 pages for each month 
for i in range(0,len(all_pages)):
    for j in range(0,len(pages)):
                 newl.append(all_pages[i] + pages[j])

newl

# 50 urls, each urls has about 10-12 articles so 50 * 10 = i should get the links of 500 articles
len(newl)

# Scrape each of the 50 webpages to only get links of the articles 
all_article_urls = [get_links_one_page(newl[i]) for i in range(0, len(newl))]


# Since lenth is 50 that means our list is a nested list 
len(all_article_urls)

# Flatten nested list 
all_article_urls = sum(all_article_urls, [])
len(all_article_urls)


# ### Scrape each of the 500 webpages and store them as a json file 
def get_file_content(url):
    response = requests.get(url)
    return response.text

all_content = [get_file_content(all_article_urls[i]) for i in range(0,len(all_article_urls))]
bs(all_content)


# Can be used to get json files
# 
# for i in range(0, len(all_content)):
#     filename = str(subset[i]) + ".json"
#     with open(filename, 'w') as json_file:
#         json.dump(file_content, json_file)




len(all_content)
dat = {'Url': all_article_urls, 'Content': all_content}

final_df = pd.DataFrame(dat)

export = final_df.to_csv("articl_dat.csv", header = None, index = False)

final_df[0:5]


final_df.to_excel("final_df.xlsx")

write.csv(final_df)

final_df.to_csv('file.csv',encoding='utf-8-sig')
final_df["Url"][1]

x = all_content[2]

import re

result = re.findall('<p style="text-align: justify;">(.*)</p>',x )
len(result)
del result[-1]
len(result)
del result[0]

lol = "".join(result)

def get_clean_content(txt):
    result = re.findall('<p style="text-align: justify;">(.*)</p>',txt)
    x = len(result) - 1
    final = "".join(result[:-1])
    return final

get_clean_content(all_content[1])
cleaned_text = [get_clean_content(all_content[i]) for i in range(0, len(all_content))]
final_df["cleaned_text"] = cleaned_text
final_df
final_df['Url'][538]



