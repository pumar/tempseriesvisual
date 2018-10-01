# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import os

cmap = plt.get_cmap('viridis')

df = pd.read_table('',
                   sep=';',
                   usecols=['Files','Date','Time','Buttons'])

df['datetime'] = df['Date'] + ' ' + df['Time']
df['datetime'] = pd.to_datetime(df['datetime'])
df = df[['Files','datetime','Buttons']]

#%%
for button in df.Buttons.unique():    
    temp_df = df[df['Buttons']==button][['Files','datetime']]
    colors = cmap(np.linspace(0, 1, len(temp_df.Files.unique())))
    fig, ax = plt.subplots()
    for (name,color) in zip(temp_df.Files.unique(),colors):
        col_df = temp_df[temp_df.Files==name]
        col_df = col_df.set_index('datetime').resample('10T').count().dropna().reset_index()
        plt.plot(col_df['datetime'],col_df['Files'],label=name,c=color)
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%d"))
    ax.xaxis.set_minor_formatter(mdates.DateFormatter("%d"))
    _=plt.xticks(rotation=90) 
    plt.legend()
    plt.savefig(os.getcwd()+'/Documents/tempseriesvisual/'+button+'_tempseries.png')
    plt.close()


#%%
