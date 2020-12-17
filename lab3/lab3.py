#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import time as t
from random import randint
import plotly.express as px


# In[2]:


multiplier = 100
bot_bound = 10 * multiplier
top_bound = 50 * multiplier


# In[3]:


def calc_average(nums: list) -> tuple:
    average=0
    for element in nums:
        average+=element
    return average
# 1 + F(Цикл)=1 + 3*n + 3*(1+1)= 3*n + 7


# In[4]:


def evaluate_results(repetitions: int) -> list:
    results = []
    for _ in range(repetitions):
        n = randint(bot_bound, top_bound)
        data = [randint(-1000000000,1000000000) for _ in range(n)]
        start_time = t.time()
        _ = calc_average(data)
        end_time = t.time()
        evaluated_time = end_time - start_time
        results.append((n, evaluated_time))
    return results


# In[5]:


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


# In[11]:


build_chart(sorted(evaluate_results(200), key=lambda tup: tup[0]))


# In[ ]:




