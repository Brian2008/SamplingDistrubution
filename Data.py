from os import stat
import plotly.figure_factory as ff
import statistics
import pandas as pd
import random
import csv
import plotly.graph_objects as go
df=pd.read_csv("Temp.csv")
data=df["temp"].tolist()

def random_set_of_mean(counter):

    dataset=[]
    for i in range(0,counter):
        random_index=random.randint(0,len(data)-1)
        value=data[random_index]
        dataset.append(value)
    mean=statistics.mean(dataset)
    return mean
def show_fig(meanList):
    df=meanList
    fig=ff.create_distplot([df],["temp"],show_hist=False)
    fig.show()
def setup():
    meanList=[]
    for i in range (0,1000):
        set_of_means=random_set_of_mean(100)
        meanList.append(set_of_means)
    show_fig(meanList)
setup()
def standardDeviation():
    meanList=[]
    for i in range (0,1000):
        set_of_means=random_set_of_mean(100)
        meanList.append(set_of_means)
    STDeviation=statistics.stdev(meanList)
    print(STDeviation)
standardDeviation()











