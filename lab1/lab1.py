#!/usr/bin/env python
# coding: utf-8

# In[4]:


import plotly.express as px
from plotly.subplots import make_subplots
import pandas as pd
import datetime as dt

blocks = [
    [2,3,4,1,2],
    [4,3,1,4,1],
    [3,2,4,2,1],
    [4,2,1,4,3],
    [3,1,2,4,1]
    ]

asyncMode = [

    dict(
        process=1,
        block=1,
        duration=dt.datetime.fromtimestamp(2).strftime('%Y-%m-%d %H:%M:%S'),
        start=dt.datetime.fromtimestamp(0).strftime('%Y-%m-%d %H:%M:%S')
    ),
    dict(
        process=1,
        block=2,
        duration=dt.datetime.fromtimestamp(5).strftime('%Y-%m-%d %H:%M:%S'),
        start=dt.datetime.fromtimestamp(2).strftime('%Y-%m-%d %H:%M:%S')
    ),
    dict(
        process=1,
        block=3,
        duration=dt.datetime.fromtimestamp(9).strftime('%Y-%m-%d %H:%M:%S'),
        start=dt.datetime.fromtimestamp(5).strftime('%Y-%m-%d %H:%M:%S')
    ),
    dict(
        process=1,
        block=4,
        duration=dt.datetime.fromtimestamp(10).strftime('%Y-%m-%d %H:%M:%S'),
        start=dt.datetime.fromtimestamp(9).strftime('%Y-%m-%d %H:%M:%S')
    ),
    dict(
        process=1,
        block=5,
        duration=dt.datetime.fromtimestamp(12).strftime('%Y-%m-%d %H:%M:%S'),
        start=dt.datetime.fromtimestamp(10).strftime('%Y-%m-%d %H:%M:%S')
    ),

    dict(
        process=2,
        block=1,
        duration=dt.datetime.fromtimestamp(6).strftime('%Y-%m-%d %H:%M:%S'),
        start=dt.datetime.fromtimestamp(2).strftime('%Y-%m-%d %H:%M:%S')
    ),
    dict(
        process=2,
        block=2,
        duration=dt.datetime.fromtimestamp(9).strftime('%Y-%m-%d %H:%M:%S'),
        start=dt.datetime.fromtimestamp(6).strftime('%Y-%m-%d %H:%M:%S')
    ),
    dict(
        process=2,
        block=3,
        duration=dt.datetime.fromtimestamp(10).strftime('%Y-%m-%d %H:%M:%S'),
        start=dt.datetime.fromtimestamp(9).strftime('%Y-%m-%d %H:%M:%S')
    ),
    dict(
        process=2,
        block=4,
        duration=dt.datetime.fromtimestamp(14).strftime('%Y-%m-%d %H:%M:%S'),
        start=dt.datetime.fromtimestamp(10).strftime('%Y-%m-%d %H:%M:%S')
    ),
    dict(
        process=2,
        block=5,
        duration=dt.datetime.fromtimestamp(15).strftime('%Y-%m-%d %H:%M:%S'),
        start=dt.datetime.fromtimestamp(14).strftime('%Y-%m-%d %H:%M:%S')
    ),

    # the third process

    dict(
        process=3,
        block=1,
        duration=dt.datetime.fromtimestamp(9).strftime('%Y-%m-%d %H:%M:%S'),
        start=dt.datetime.fromtimestamp(6).strftime('%Y-%m-%d %H:%M:%S')
    ),
    dict(
        process=3,
        block=2,
        duration=dt.datetime.fromtimestamp(11).strftime('%Y-%m-%d %H:%M:%S'),
        start=dt.datetime.fromtimestamp(9).strftime('%Y-%m-%d %H:%M:%S')
    ),
    dict(
        process=3,
        block=3,
        duration=dt.datetime.fromtimestamp(15).strftime('%Y-%m-%d %H:%M:%S'),
        start=dt.datetime.fromtimestamp(11).strftime('%Y-%m-%d %H:%M:%S')
    ),
    dict(
        process=3,
        block=4,
        duration=dt.datetime.fromtimestamp(17).strftime('%Y-%m-%d %H:%M:%S'),
        start=dt.datetime.fromtimestamp(15).strftime('%Y-%m-%d %H:%M:%S')
    ),
    dict(
        process=3,
        block=5,
        duration=dt.datetime.fromtimestamp(18).strftime('%Y-%m-%d %H:%M:%S'),
        start=dt.datetime.fromtimestamp(17).strftime('%Y-%m-%d %H:%M:%S')
    ),

    dict(
        process=4,
        block=1,
        duration=dt.datetime.fromtimestamp(13).strftime('%Y-%m-%d %H:%M:%S'),
        start=dt.datetime.fromtimestamp(9).strftime('%Y-%m-%d %H:%M:%S') 
    ),
    dict(
        process=4,
        block=2,
        duration=dt.datetime.fromtimestamp(15).strftime('%Y-%m-%d %H:%M:%S'),
        start=dt.datetime.fromtimestamp(13).strftime('%Y-%m-%d %H:%M:%S')
    ),
    dict(
        process=4,
        block=3,
        duration=dt.datetime.fromtimestamp(16).strftime('%Y-%m-%d %H:%M:%S'),
        start=dt.datetime.fromtimestamp(15).strftime('%Y-%m-%d %H:%M:%S')
    ),
    dict(
        process=4,
        block=4,
        duration=dt.datetime.fromtimestamp(21).strftime('%Y-%m-%d %H:%M:%S'),
        start=dt.datetime.fromtimestamp(17).strftime('%Y-%m-%d %H:%M:%S')
    ),
    dict(
        process=4,
        block=5,
        duration=dt.datetime.fromtimestamp(24).strftime('%Y-%m-%d %H:%M:%S'),
        start=dt.datetime.fromtimestamp(21).strftime('%Y-%m-%d %H:%M:%S')
    ),

    dict(
        process=5,
        block=1,
        duration=dt.datetime.fromtimestamp(16).strftime('%Y-%m-%d %H:%M:%S'),
        start=dt.datetime.fromtimestamp(13).strftime('%Y-%m-%d %H:%M:%S') 
    ),
    dict(
        process=5,
        block=2,
        duration=dt.datetime.fromtimestamp(17).strftime('%Y-%m-%d %H:%M:%S'),
        start=dt.datetime.fromtimestamp(16).strftime('%Y-%m-%d %H:%M:%S')
    ),
    dict(
        process=5,
        block=3,
        duration=dt.datetime.fromtimestamp(19).strftime('%Y-%m-%d %H:%M:%S'),
        start=dt.datetime.fromtimestamp(17).strftime('%Y-%m-%d %H:%M:%S')
    ),
    dict(
        process=5,
        block=4,
        duration=dt.datetime.fromtimestamp(25).strftime('%Y-%m-%d %H:%M:%S'),
        start=dt.datetime.fromtimestamp(21).strftime('%Y-%m-%d %H:%M:%S')
    ),
    dict(
        process=5,
        block=5,
        duration=dt.datetime.fromtimestamp(26).strftime('%Y-%m-%d %H:%M:%S'),
        start=dt.datetime.fromtimestamp(25).strftime('%Y-%m-%d %H:%M:%S')
    ),
]

sync1Mode = [

    dict(
        process=1,
        block=1,
        duration=dt.datetime.fromtimestamp(2).strftime('%Y-%m-%d %H:%M:%S'),
        start=dt.datetime.fromtimestamp(0).strftime('%Y-%m-%d %H:%M:%S')
    ),
    dict(
        process=1,
        block=2,
        duration=dt.datetime.fromtimestamp(5).strftime('%Y-%m-%d %H:%M:%S'),
        start=dt.datetime.fromtimestamp(2).strftime('%Y-%m-%d %H:%M:%S')
    ),
    dict(
        process=1,
        block=3,
        duration=dt.datetime.fromtimestamp(9).strftime('%Y-%m-%d %H:%M:%S'),
        start=dt.datetime.fromtimestamp(5).strftime('%Y-%m-%d %H:%M:%S')
    ),
    dict(
        process=1,
        block=4,
        duration=dt.datetime.fromtimestamp(10).strftime('%Y-%m-%d %H:%M:%S'),
        start=dt.datetime.fromtimestamp(9).strftime('%Y-%m-%d %H:%M:%S')
    ),
    dict(
        process=1,
        block=5,
        duration=dt.datetime.fromtimestamp(12).strftime('%Y-%m-%d %H:%M:%S'),
        start=dt.datetime.fromtimestamp(10).strftime('%Y-%m-%d %H:%M:%S')
    ),

    dict(
        process=2,
        block=1,
        duration=dt.datetime.fromtimestamp(6).strftime('%Y-%m-%d %H:%M:%S'),
        start=dt.datetime.fromtimestamp(2).strftime('%Y-%m-%d %H:%M:%S')
    ),
    dict(
        process=2,
        block=2,
        duration=dt.datetime.fromtimestamp(9).strftime('%Y-%m-%d %H:%M:%S'),
        start=dt.datetime.fromtimestamp(6).strftime('%Y-%m-%d %H:%M:%S')
    ),
    dict(
        process=2,
        block=3,
        duration=dt.datetime.fromtimestamp(10).strftime('%Y-%m-%d %H:%M:%S'),
        start=dt.datetime.fromtimestamp(9).strftime('%Y-%m-%d %H:%M:%S')
    ),
    dict(
        process=2,
        block=4,
        duration=dt.datetime.fromtimestamp(14).strftime('%Y-%m-%d %H:%M:%S'),
        start=dt.datetime.fromtimestamp(10).strftime('%Y-%m-%d %H:%M:%S')
    ),
    dict(
        process=2,
        block=5,
        duration=dt.datetime.fromtimestamp(15).strftime('%Y-%m-%d %H:%M:%S'),
        start=dt.datetime.fromtimestamp(14).strftime('%Y-%m-%d %H:%M:%S')
    ),

    dict(
        process=3,
        block=1,
        duration=dt.datetime.fromtimestamp(9).strftime('%Y-%m-%d %H:%M:%S'),
        start=dt.datetime.fromtimestamp(6).strftime('%Y-%m-%d %H:%M:%S')
    ),
    dict(
        process=3,
        block=2,
        duration=dt.datetime.fromtimestamp(11).strftime('%Y-%m-%d %H:%M:%S'),
        start=dt.datetime.fromtimestamp(9).strftime('%Y-%m-%d %H:%M:%S')
    ),
    dict(
        process=3,
        block=3,
        duration=dt.datetime.fromtimestamp(15).strftime('%Y-%m-%d %H:%M:%S'),
        start=dt.datetime.fromtimestamp(11).strftime('%Y-%m-%d %H:%M:%S')
    ),
    dict(
        process=3,
        block=4,
        duration=dt.datetime.fromtimestamp(17).strftime('%Y-%m-%d %H:%M:%S'),
        start=dt.datetime.fromtimestamp(15).strftime('%Y-%m-%d %H:%M:%S')
    ),
    dict(
        process=3,
        block=5,
        duration=dt.datetime.fromtimestamp(18).strftime('%Y-%m-%d %H:%M:%S'),
        start=dt.datetime.fromtimestamp(17).strftime('%Y-%m-%d %H:%M:%S')
    ),

    dict(
        process=4,
        block=1,
        duration=dt.datetime.fromtimestamp(14).strftime('%Y-%m-%d %H:%M:%S'),
        start=dt.datetime.fromtimestamp(10).strftime('%Y-%m-%d %H:%M:%S') 
    ),
    dict(
        process=4,
        block=2,
        duration=dt.datetime.fromtimestamp(16).strftime('%Y-%m-%d %H:%M:%S'),
        start=dt.datetime.fromtimestamp(14).strftime('%Y-%m-%d %H:%M:%S')
    ),
    dict(
        process=4,
        block=3,
        duration=dt.datetime.fromtimestamp(17).strftime('%Y-%m-%d %H:%M:%S'),
        start=dt.datetime.fromtimestamp(16).strftime('%Y-%m-%d %H:%M:%S')
    ),
    dict(
        process=4,
        block=4,
        duration=dt.datetime.fromtimestamp(21).strftime('%Y-%m-%d %H:%M:%S'),
        start=dt.datetime.fromtimestamp(17).strftime('%Y-%m-%d %H:%M:%S')
    ),
    dict(
        process=4,
        block=5,
        duration=dt.datetime.fromtimestamp(24).strftime('%Y-%m-%d %H:%M:%S'),
        start=dt.datetime.fromtimestamp(21).strftime('%Y-%m-%d %H:%M:%S')
    ),

    dict(
        process=5,
        block=1,
        duration=dt.datetime.fromtimestamp(18).strftime('%Y-%m-%d %H:%M:%S'),
        start=dt.datetime.fromtimestamp(15).strftime('%Y-%m-%d %H:%M:%S') 
    ),
    dict(
        process=5,
        block=2,
        duration=dt.datetime.fromtimestamp(19).strftime('%Y-%m-%d %H:%M:%S'),
        start=dt.datetime.fromtimestamp(18).strftime('%Y-%m-%d %H:%M:%S')
    ),
    dict(
        process=5,
        block=3,
        duration=dt.datetime.fromtimestamp(21).strftime('%Y-%m-%d %H:%M:%S'),
        start=dt.datetime.fromtimestamp(19).strftime('%Y-%m-%d %H:%M:%S')
    ),
    dict(
        process=5,
        block=4,
        duration=dt.datetime.fromtimestamp(25).strftime('%Y-%m-%d %H:%M:%S'),
        start=dt.datetime.fromtimestamp(21).strftime('%Y-%m-%d %H:%M:%S')
    ),
    dict(
        process=5,
        block=5,
        duration=dt.datetime.fromtimestamp(26).strftime('%Y-%m-%d %H:%M:%S'),
        start=dt.datetime.fromtimestamp(25).strftime('%Y-%m-%d %H:%M:%S')
    ),
]

sync2Mode = [
    
    dict(
        process=1,
        block=1,
        duration=dt.datetime.fromtimestamp(2).strftime('%Y-%m-%d %H:%M:%S'),
        start=dt.datetime.fromtimestamp(0).strftime('%Y-%m-%d %H:%M:%S')
    ),
    dict(
        process=1,
        block=2,
        duration=dt.datetime.fromtimestamp(11).strftime('%Y-%m-%d %H:%M:%S'),
        start=dt.datetime.fromtimestamp(8).strftime('%Y-%m-%d %H:%M:%S')
    ),
    dict(
        process=1,
        block=3,
        duration=dt.datetime.fromtimestamp(15).strftime('%Y-%m-%d %H:%M:%S'),
        start=dt.datetime.fromtimestamp(11).strftime('%Y-%m-%d %H:%M:%S')
    ),
    dict(
        process=1,
        block=4,
        duration=dt.datetime.fromtimestamp(16).strftime('%Y-%m-%d %H:%M:%S'),
        start=dt.datetime.fromtimestamp(15).strftime('%Y-%m-%d %H:%M:%S')
    ),
    dict(
        process=1,
        block=5,
        duration=dt.datetime.fromtimestamp(25).strftime('%Y-%m-%d %H:%M:%S'),
        start=dt.datetime.fromtimestamp(23).strftime('%Y-%m-%d %H:%M:%S')
    ),

    # the second process

    dict(
        process=2,
        block=1,
        duration=dt.datetime.fromtimestamp(6).strftime('%Y-%m-%d %H:%M:%S'),
        start=dt.datetime.fromtimestamp(2).strftime('%Y-%m-%d %H:%M:%S')
    ),
    dict(
        process=2,
        block=2,
        duration=dt.datetime.fromtimestamp(13).strftime('%Y-%m-%d %H:%M:%S'),
        start=dt.datetime.fromtimestamp(11).strftime('%Y-%m-%d %H:%M:%S')
    ),
    dict(
        process=2,
        block=3,
        duration=dt.datetime.fromtimestamp(16).strftime('%Y-%m-%d %H:%M:%S'),
        start=dt.datetime.fromtimestamp(15).strftime('%Y-%m-%d %H:%M:%S')
    ),
    dict(
        process=2,
        block=4,
        duration=dt.datetime.fromtimestamp(20).strftime('%Y-%m-%d %H:%M:%S'),
        start=dt.datetime.fromtimestamp(16).strftime('%Y-%m-%d %H:%M:%S')
    ),
    dict(
        process=2,
        block=5,
        duration=dt.datetime.fromtimestamp(26).strftime('%Y-%m-%d %H:%M:%S'),
        start=dt.datetime.fromtimestamp(25).strftime('%Y-%m-%d %H:%M:%S')
    ),

    dict(
        process=3,
        block=1,
        duration=dt.datetime.fromtimestamp(9).strftime('%Y-%m-%d %H:%M:%S'),
        start=dt.datetime.fromtimestamp(6).strftime('%Y-%m-%d %H:%M:%S')
    ),
    dict(
        process=3,
        block=2,
        duration=dt.datetime.fromtimestamp(15).strftime('%Y-%m-%d %H:%M:%S'),
        start=dt.datetime.fromtimestamp(13).strftime('%Y-%m-%d %H:%M:%S')
    ),
    dict(
        process=3,
        block=3,
        duration=dt.datetime.fromtimestamp(20).strftime('%Y-%m-%d %H:%M:%S'),
        start=dt.datetime.fromtimestamp(16).strftime('%Y-%m-%d %H:%M:%S')
    ),
    dict(
        process=3,
        block=4,
        duration=dt.datetime.fromtimestamp(22).strftime('%Y-%m-%d %H:%M:%S'),
        start=dt.datetime.fromtimestamp(20).strftime('%Y-%m-%d %H:%M:%S')
    ),
    dict(
        process=3,
        block=5,
        duration=dt.datetime.fromtimestamp(27).strftime('%Y-%m-%d %H:%M:%S'),
        start=dt.datetime.fromtimestamp(26).strftime('%Y-%m-%d %H:%M:%S')
    ),

    dict(
        process=4,
        block=1,
        duration=dt.datetime.fromtimestamp(13).strftime('%Y-%m-%d %H:%M:%S'),
        start=dt.datetime.fromtimestamp(9).strftime('%Y-%m-%d %H:%M:%S') 
    ),
    dict(
        process=4,
        block=2,
        duration=dt.datetime.fromtimestamp(16).strftime('%Y-%m-%d %H:%M:%S'),
        start=dt.datetime.fromtimestamp(15).strftime('%Y-%m-%d %H:%M:%S')
    ),
    dict(
        process=4,
        block=3,
        duration=dt.datetime.fromtimestamp(21).strftime('%Y-%m-%d %H:%M:%S'),
        start=dt.datetime.fromtimestamp(20).strftime('%Y-%m-%d %H:%M:%S')
    ),
    dict(
        process=4,
        block=4,
        duration=dt.datetime.fromtimestamp(26).strftime('%Y-%m-%d %H:%M:%S'),
        start=dt.datetime.fromtimestamp(22).strftime('%Y-%m-%d %H:%M:%S')
    ),
    dict(
        process=4,
        block=5,
        duration=dt.datetime.fromtimestamp(30).strftime('%Y-%m-%d %H:%M:%S'),
        start=dt.datetime.fromtimestamp(27).strftime('%Y-%m-%d %H:%M:%S')
    ),

    dict(
        process=5,
        block=1,
        duration=dt.datetime.fromtimestamp(16).strftime('%Y-%m-%d %H:%M:%S'),
        start=dt.datetime.fromtimestamp(13).strftime('%Y-%m-%d %H:%M:%S') 
    ),
    dict(
        process=5,
        block=2,
        duration=dt.datetime.fromtimestamp(18).strftime('%Y-%m-%d %H:%M:%S'),
        start=dt.datetime.fromtimestamp(16).strftime('%Y-%m-%d %H:%M:%S')
    ),
    dict(
        process=5,
        block=3,
        duration=dt.datetime.fromtimestamp(23).strftime('%Y-%m-%d %H:%M:%S'),
        start=dt.datetime.fromtimestamp(21).strftime('%Y-%m-%d %H:%M:%S')
    ),
    dict(
        process=5,
        block=4,
        duration=dt.datetime.fromtimestamp(30).strftime('%Y-%m-%d %H:%M:%S'),
        start=dt.datetime.fromtimestamp(26).strftime('%Y-%m-%d %H:%M:%S')
    ),
    dict(
        process=5,
        block=5,
        duration=dt.datetime.fromtimestamp(31).strftime('%Y-%m-%d %H:%M:%S'),
        start=dt.datetime.fromtimestamp(30).strftime('%Y-%m-%d %H:%M:%S')
    ),
]

c_df = pd.DataFrame(asyncMode)
c_fig = px.timeline(c_df, x_start="start", x_end="duration", y="process", color="block")
c_fig.show()

c_df = pd.DataFrame(sync1Mode)
c_fig = px.timeline(c_df, x_start="start", x_end="duration", y="process", color="block")
c_fig.show()

c_df = pd.DataFrame(sync2Mode)
c_fig = px.timeline(c_df, x_start="start", x_end="duration", y="process", color="block")
c_fig.show()


# In[2]:


def critical(matrix):
    i=j=0
    time = matrix[0][0]
    
    while i < len(matrix) - 1:
        while j < len(matrix) - 1:
            if matrix[i][j+1] > matrix[i+1][j]:
                j+=1
                time += matrix[i][j]
                continue
            else:
                time += matrix[i+1][j]
                break
        i+=1
    return time


# In[7]:


print(critical(blocks))


# In[ ]:




