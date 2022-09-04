"""
==============
Data Extraction with graph
==============

This example shows how to extract data from dataframe columns  in csv file and use it to create scatter 
.

Reference:
`
'For bar chart creation':
https://matplotlib.org/stable/gallery/lines_bars_and_markers/
bar_label_demo.html

"""

import json
import csv
import matplotlib as plt
from matplotlib import pyplot
import pandas as pd


def get_csv_file():
    with open (r'C:\Users\prema\Desktop\for_graph_scatter1.csv','r') as j:
        file_csv = pd.read_csv(j)
    return file_csv

def get_df_InitX():
    df = pd.DataFrame(get_csv_file())
    return df['ShiftedX(Init)']

    
def get_df_InitY():
   df = pd.DataFrame(get_csv_file())
   return df['ShiftedY(Init)']

def get_df_FinalX():
   df = pd.DataFrame(get_csv_file())
   return df['ShiftedX(Final)']

def get_df_FinalY():
   df = pd.DataFrame(get_csv_file())
   return df['ShiftedY(Final)']          

def plot_freq_graph():
    fig,ax=plt.pyplot.subplots()
    ax.set_xlabel('Position X')
    ax.set_ylabel('Position Y')
    ax.set_title('Scatter_Plot: Initial Position and Final Position')
    scatter_plot= ax.scatter(get_df_InitX(), get_df_InitY(),alpha=0.5)
    scatter_plot = ax.scatter(get_df_FinalX(),get_df_FinalY(),alpha=0.5)
    ax.set_xlim(-0.8,0.8)
    ax.set_ylim(-0.8,0.8)
    ax.grid(True)
    #hrz_bar = ax.barh(list(create_freq().keys()), list(create_freq().values()),align='center')
    
    return plt.pyplot.show()

plot_freq_graph()






