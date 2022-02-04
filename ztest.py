from pip import main
import plotly.figure_factory as ff
import plotly.graph_objects as go
import pandas as pd
import csv
import statistics
import random

df = pd.read_csv("medium_data.csv")

data = df["reading_time"].tolist()

#fig = ff.create_distplot([data], ["Math_score"], show_hist= False)
#fig.show()

mean = statistics.mean(data)

std_deviation = statistics.stdev(data)

print("Mean of population :", mean)
print("Standard Deviation of population : ", std_deviation)

def random_set_mean(counter):
    dataset = []
    for i in range(0, counter):
        random_index = random.randint(0, len(data)-1)
        value = data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean


mean_list = []
for i in range(0, 1000):
    set_of_means = random_set_mean(100)
    mean_list.append(set_of_means)




std_deviation = statistics.stdev(mean_list) 
mean = statistics.mean(mean_list)

print("Mean of Sample distribution :", mean)
print("Standard deviation of sampling distribution :", std_deviation)




fig =ff.create_distplot([mean_list], ["reading_time"], show_hist= False)
fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.20], mode="lines", name="MEAN"))
fig.show()


first_std_deviation_start, first_std_deviation_end = mean-std_deviation, mean+std_deviation
second_std_deviation_start, second_std_deviation_end = mean-(2*std_deviation), mean+(2*std_deviation)
third_std_deviation_start, third_std_deviation_end = mean-(3*std_deviation), mean+(3*std_deviation)

print("std1",first_std_deviation_start, first_std_deviation_end)
print("std2",second_std_deviation_start, second_std_deviation_end)
print("std3",third_std_deviation_start, third_std_deviation_end)

fig= ff.create_distplot([mean_list], ["reading_time"], show_hist= False)
fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.17], mode= "lines", name= "Mean"))

fig.add_trace(go.Scatter(x=[first_std_deviation_start, first_std_deviation_start], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1 START"))
fig.add_trace(go.Scatter(x=[first_std_deviation_end, first_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1 END"))
fig.add_trace(go.Scatter(x=[second_std_deviation_start, second_std_deviation_start], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2 START"))
fig.add_trace(go.Scatter(x=[second_std_deviation_end, second_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2 END"))
fig.add_trace(go.Scatter(x=[third_std_deviation_start, third_std_deviation_start], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 3 START"))
fig.add_trace(go.Scatter(x=[third_std_deviation_end, third_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 3 END"))

fig.show()

