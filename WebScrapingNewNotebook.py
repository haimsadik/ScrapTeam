
# coding: utf-8

# # WebScraping Notebook Ben

# In[9]:


#On télecharge les packages dont on va avoir besoin
import selenium #pip install selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By  
import time
#BeautifulSoup , Request et Pandas
import urllib
import bs4
from urllib import request
import pandas 
#pour les graphiques
get_ipython().magic('matplotlib inline')
import matplotlib.pyplot as plt
import numpy as np


# In[65]:


path_to_web_driver = "/Users/SADIK/Desktop/PythonWebScrap/chromedriver"
browser = webdriver.Chrome(path_to_web_driver)
browser.get('http://www.matchendirect.fr/resultat-foot-21-01-2018/')


# In[14]:


#Lecture de la page 

#On récupère le texte et l'id de la page suivante, qui apparait comme standardisé
lien='http://www.matchendirect.fr/resultat-foot-21-01-2018/'
request_text = request.urlopen(lien).read()
page = bs4.BeautifulSoup(request_text, "lxml")
# request_text c'est trop dégueu
#  page.find('div', {'class':'pagination'}).find('a')['href']


# In[79]:


# page.find('div', {'class':'events'}).findAll('a')

#s1=page.findAll('div',{"class": 'panel-body'})
#s2=s1.findAll('table',{'class':'table table striped table-hover'})
# s=page.findAll('td',{'class':'panel-body table table-striped table-hover lm1'})
PageTime=page.find_all('div', class_ = 'panel-body')
#print(s[1])
#print(s[1].table.td)
Time=PageTime[1].find_all('td',class_="lm1")
print(t[0].text)


# In[122]:


PageAdversaire = page.find_all('div', class_ = 'panel-body')
PageAdversaire1 = PageAdversaire[1].find_all('a',href="/live-score/saint-etienne-nice.html")
print(PageAdversaire1[0].find_all('span',class_='lm3_eq1')[0].text)      
print(PageAdversaire1[0].find_all('span',class_='lm3_score')[0].text)      
print(PageAdversaire1[0].find_all('span',class_='lm3_eq2')[0].text)      

