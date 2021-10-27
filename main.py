import statistics
import plotly.figure_factory as ff
import plotly.graph_objects as go
import pandas as pd
import csv
import random
df=pd.read_csv("studentMarks.csv")

data=df["Math_score"].to_list()

mean=statistics.mean(data)
standardDivision=statistics.stdev(data)

def random_set_of_mean(counter):
    dataSet=[]
    for i in range(0,counter):
        random_index=random.randint(0,len(data)-1)
        value=data[random_index]
        dataSet.append(value)
    mean=statistics.mean(dataSet)
    return mean
mean_list=[]
for i in range(0,1000):
    setOfMeans=random_set_of_mean(100)
    mean_list.append(setOfMeans)
standardDivision=statistics.stdev(mean_list)


first_standard_division_start,first_standard_division_end=mean-standardDivision,mean+standardDivision 
standard_division_start,second_standard_division_end=mean-(2*standardDivision),mean+(2*standardDivision)
standard_division_start,third_standard_division_end=mean-(3*standardDivision),mean+(3*standardDivision)\


df=pd.read_csv("data3.csv")

data=df["Math_score"].to_list()
mean_sample3=statistics.mean(data)
print("mean of sample 3",mean_sample3)
fig=ff.create_distplot([mean_list],["students marks"],show_hist=False)
fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.17],mode="lines",name="MEAN"))
fig.add_trace(go.Scatter(x=[mean_sample3,mean_sample3],y=[0,0.17],mode="lines",name="MEAN OF STUDENTS WHO GOT FUN SHEETS"))
fig.add_trace(go.Scatter(x=[second_standard_division_end,second_standard_division_end],y=[0,0.17],mode="lines",name="STANDARD DIVISON 2 END"))
fig.add_trace(go.Scatter(x=[third_standard_division_end,third_standard_division_end],y=[0,0.17],mode="lines",name="STANDARD DIVISON 3 END"))
fig.show()