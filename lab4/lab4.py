#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import time as t
from random import randint
import plotly.express as px
import re

bot_bound = 0
top_bound = 100


# In[2]:


def binary_search(data: list, number: int):

    mid = len(data) // 2
    low = 0
    high = len(data) - 1
    start_time = t.time()
    
    data.sort()
            
    while data[mid] != number and low <= high:
        if number > data[mid]:
            low = mid + 1
        else:
            high = mid - 1
        mid = (low + high) // 2

    if low > high:
        print("Ключ не найден")
    else:
        print(f"Ключ {mid} найден")
        
    finish_time = t.time()
    
    return finish_time - start_time

# = 1 + 3*(n-1) + (n-1)*f(Цикл for по j) = 1 + 3*(n-1) + (n-1)*(1 + 3*(n-1) + (n-1)*(2+2+1+2+2+2+2+1)) =
# = 1+3n-3+(n-1)*(1+3n-3+14n-14)=-2+3n+(n-1)*(17n-16)=2 + 3n + 17n^2 - 33*n + 16 = 17n^2 - 30*n + 18

# = 1 + 3*n + n*f(Цикл while)=1 + 3*n + n*()= 14*n+1

# = 1


#17n^2 + -16n + 20


# In[3]:


array = [randint(0,100) for _ in range(20)]
time = binary_search(array, 100)
print(f"Время выполнения алгоритма: {time} секунд")


# In[4]:


def evaluate_results(repetitions: int) -> list:
    results = []
    n=0
    for _ in range(repetitions):
        n+=5000
        data = [randint(0,100) for _ in range(n)]
        random_number=randint(0,1000)
        start_time = t.time()
        evaluated_time = binary_search(data, random_number)
        finish_time = t.time()
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


# In[8]:


build_chart(sorted(evaluate_results(100), key=lambda tup: tup[0]))


# In[ ]:





# In[ ]:




