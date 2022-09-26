#!/usr/bin/env python
# coding: utf-8

# # web scraping

# ## Importing packages

# In[ ]:


### from bs4 import BeautifulSoup
import requests
import pandas as pd


# ### Function to extract the data

# In[161]:


def webscraping():
    for i in range(1,26):
        
        url="https://stats.espncricinfo.com/ci/engine/stats/index.html?class=3;page="+str(i)+";template=results;type=aggregate;view=results"
        r=requests.get(url)
        #html_content
        page_content=r.text
        soup=BeautifulSoup(page_content,"html.parser")
        #for entire dataset data processing.....
        tr_data =soup.find_all('tr',{'class':'data1'})
        #dataset=[]
        for i in tr_data:
            raw_list=i.text.replace('\n',',').strip().split(",")
            raw_list.pop(5)
            raw_list.pop(0)
            raw_list.pop()
            raw_list.pop()
            dataset.append(raw_list)

dataset=[]      
webscraping()
print("successful")


# In[166]:


df=pd.DataFrame(dataset,columns=["Winner",'Result',"Margin","BR","Match","Ground","Start Date"])
print("no.of total records",len(df))


# In[165]:


df


# In[ ]:


url="https://stats.espncricinfo.com/ci/engine/stats/index.html?class=3;page=2;template=results;type=aggregate;view=results"


# In[ ]:


r=requests.get(url)
r.status_code
#html_content
page_content=r.text


# In[ ]:


soup=BeautifulSoup(page_content,"html.parser")
#print(len(soup))
#soup
#soup.prettify()


# In[ ]:


soup.title.text


# In[ ]:


titles=[]
tr_tags=soup.find_all('tr',{'class':"headlinks"})
for i in tr_tags:
    titles.append(i.text.replace("\n",' ').strip())
    
final_titles=titles1[0].split()

final_titles


# In[ ]:


tr_data = soup.find_all('tr',{'class':'data1'})
#len(tr_data)
first=tr_data[3]
final=(first.text.replace('\n',',').strip().split(','))
new_final=final.pop(5)
final.pop(0)
final.pop()
final.pop()
print(final)
#filter the empty string in list
filteredlist=list(filter(None,final))
#print(type(first.text))

data=[]
#filteredlist
#for i in first:
#    data.append(i.text)
#data
    
    


# In[ ]:


#for entire dataset data processing.....
tr_data =soup.find_all('tr',{'class':'data1'})
dataset=[]
for i in tr_data:
    #print(i.text)
    raw_list=i.text.replace('\n',',').strip().split(",")
    raw_list.pop(5)
    #print(raw_list)
    raw_list.pop(0)
    raw_list.pop()
    raw_list.pop()
    #raw_list=list(filter(None,raw_list))
    #print(filterdlist)
    
    dataset.append(raw_list)
dataset[:3]
    


# In[ ]:


tr_data[6]


# #create dataset using pandas
# import pandas as pd

# In[ ]:


df=pd.DataFrame(dataset,columns=["Winner",'Result',"Margin","BR","Match","Ground","Start Date"])
df


# In[ ]:


#next page 
page2=soup.find_all('a',class_="PaginationLink")
for i in page2:
    print(len(i['href']))

