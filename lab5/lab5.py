#!/usr/bin/env python
# coding: utf-8

# In[6]:


import numpy as np
import time as t
from random import randint
import plotly.express as px
import re


# In[7]:


def binary_search_recursive(data, elem, start=0, end=None):
    data.sort()
    
    #1
    if end is None:
        #1+1
        end = len(data) - 1
    #1
    if start > end:
        print("Ключ не найден")
        return False

    #1+1+1
    mid = (start + end) // 2
    
    #2+1
    if elem == data[mid]:
        print(f"Ключ {mid} найден")
        return mid
    #2+1+1
    if elem < data[mid]:
        return binary_search_recursive(data, elem, start, mid-1)
    
    #1
    return binary_search_recursive(data, elem, mid+1, end)

# O(15n) ~ O(n)


# In[8]:


array = [randint(0,10) for _ in range(5)]
start_time = t.time()
binary_search_recursive(array, 5)
finish_time = t.time()

print (array)
print(finish_time-start_time)


# In[9]:


def evaluate_results(repetitions: int) -> list:
    results = []
    n=0
    for _ in range(repetitions):
        n+=5000
        data = [randint(0,100) for _ in range(n)]
        random_number=randint(0,100)
        start_time = t.time()
        evaluated_time = binary_search_recursive(data, random_number)
        finish_time = t.time()
        results.append((n, finish_time - start_time))
    return results


# In[10]:


def build_chart(raw):
    chart_data = []

    for (n, time) in raw:
        chart_data.append(
            dict(
                size=n,
                evaluation=time
            )
        )
    fig = px.line(chart_data, x="size", y="evaluation")
    fig.show()


# In[12]:


build_chart(sorted(evaluate_results(100), key=lambda tup: tup[0]))


# In[ ]:




