"""
==============
Data Extraction with graph
==============

This example shows how to extract text data from web scraping ,use it 
to analyze frequency of keywords and display it in horizontal bar chart .

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




def get_file():
    text_tweet=''
    for i in range(0,15):
        with open ('save_1.json','r') as k:
            open_1 = json.load(k)
        text_tweet=text_tweet + open_1['statuses'][i]['text']
    return text_tweet.split()
          


def lexicon_words():
    list_words=[]
    with open('lexicon.csv',newline='') as k:
        for row in csv.reader(k):
            list_words.append(row[0])
        return list_words

def create_freq():
    freq_str = {}
    for i in lexicon_words():
        if i in get_file() and i not in freq_str:
            freq_str[str(i)]=1
        if i not in get_file():
            freq_str[str(i)]=0
        else:
            freq_str[str(i)]= freq_str[str(i)] + 1
    return freq_str

def plot_freq_graph():
    fig,ax=plt.pyplot.subplots()
    ax.set_xlabel('Summation')
    ax.set_ylabel(' KeyWords')
    ax.set_title('Horizontal Bar Chart:Keywords analysis from extracted text')
    hrz_bar = ax.barh(list(create_freq().keys()), list(create_freq().values()),align='center')
    
    return plt.pyplot.show()
plot_freq_graph()




