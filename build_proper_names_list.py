
# coding: utf-8

# In[1]:

import os
import re
import sys


# In[2]:

phi5_path_rel = '~/cltk_data/compiled/phi5/'
phi5_path_abs = os.path.expanduser(phi5_path_rel)
phi5_files = os.listdir(phi5_path_abs)


# In[3]:

d = re.compile(r'([a-z]\s)([A-Z][a-zA-Z0-9_]+)')


# In[4]:

names_list = []
for phi5_file in phi5_files:
    if phi5_file.startswith('LAT') and phi5_file.endswith('.txt'):
        file_path = phi5_path_abs + phi5_file
        with open(file_path) as f:
            opened_txt = f.read()
            propers = d.findall(opened_txt)
            for name in propers:
                names_list.append(name[1])


# In[5]:

sorted_alpha_set = sorted(set(names_list))


# In[6]:

newlines_str = '\n'.join(sorted_alpha_set)


# In[7]:

with open('proper_names.txt', 'w') as f:
    f.write(newlines_str)


