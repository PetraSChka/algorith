#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import time as t
from random import randint
import plotly.express as px
import re


# In[36]:


def fast_bubble_sort(data: list) -> list:
    for i in range(len(data) - 1, 0, -1):
        no_swap = True
        for j in range(i):
            if data[j + 1] < data[j]:
                data[j], data[j + 1] = data[j + 1], data[j]
                no_swap = False
        if no_swap:
            return
        
# n^2
data=[1,4,2,5,4,0,4,0]
fast_bubble_sort(data)
print (data)


# In[3]:


def evaluate_results_buble(repetitions: int) -> list:
    results = []
    n=0
    for _ in range(repetitions):
        n+=1000
        data = [randint(0,100) for _ in range(n)]
        start_time = t.time()
        evaluated_time = fast_bubble_sort(data)
        finish_time = t.time()
        results.append((n, finish_time - start_time))
    return results

#


# In[35]:


def quicksort(data, start, end):
    if end - start > 1:
        p = partition(data, start, end)
        quicksort(data, start, p)
        quicksort(data, p + 1, end)
 
 
def partition(data, start, end):
    pivot = data[start]
    i = start + 1
    j = end - 1
 
    while True:
        while (i <= j and data[i] <= pivot):
            i = i + 1
        while (i <= j and data[j] >= pivot):
            j = j - 1
 
        if i <= j:
            data[i], data[j] = data[j], data[i]
        else:
            data[start], data[j] = data[j], data[start]
            return j

    
data=[1,4,2,7,4,0]
quicksort(data,0,len(data))
print (data)
# n log n
# n^2


# In[23]:


def evaluate_results_quick(repetitions: int) -> list:
    results = []
    n=0
    for _ in range(repetitions):
        n+=5000
        data = [randint(0,100) for _ in range(n)]
        start_time = t.time()
        evaluated_time = quicksort(data,0,len(data))
        finish_time = t.time()
        results.append((n, finish_time - start_time))
    return results


# In[21]:


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


# In[37]:


build_chart(sorted(evaluate_results_buble(5), key=lambda x: x[0]))


# In[38]:


build_chart(sorted(evaluate_results_quick(20), key=lambda x: x[0]))


# In[ ]:




