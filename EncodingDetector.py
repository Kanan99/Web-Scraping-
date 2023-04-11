#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os 
import chardet


# In[15]:


for txt_name in os.listdir('txts'):
    
    with open(txt_name, 'rb') as f:
    content = f.read()
    encoding = chardet.detect(content)['encoding']

with open('txt_name', 'r', encoding=encoding) as f:
    text = f.read()
    


# In[16]:


chardet.detect(content)


# In[ ]:




