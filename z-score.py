#importing 
import random
import statistics
import plotly.graph_objects as go
import plotly.figure_factory as ff
import pandas as pd
import csv

#Reading the file and converting the necessary data into a list 
dataFrames = pd.read_csv("mediumArticle.csv")
data = dataFrames["reading_time"].tolist()

#Population mean 
populationMean = statistics.mean(data)
print("Population mean of the data file: ", populationMean)

#Finding the mean of random 30 data points
def randomSetofMean(counter):
    dataSet = []
    for i in range(0, counter):
        random_index = random.randint(0, len(data)-1)
        value = data[random_index]
        dataSet.append(value)
    meanOfRandom30DataPoints = statistics.mean(dataSet)    
    return meanOfRandom30DataPoints

#Repeating the process 100 times
meanList = []
for i in range(0, 100):
    set_of_means= randomSetofMean(30)
    meanList.append(set_of_means)

#Finding the mean and standard deviation
stdDev = statistics.stdev(meanList)
sampleMean = statistics.mean(meanList)
print("Mean of the sampling distribution: ", sampleMean)
print("Standard Deviation of sampling distribution: ", stdDev)

#Finding the standard deviation start and end values
first_std_deviation_start, first_std_deviation_end = sampleMean-stdDev, sampleMean+stdDev
second_std_deviation_start, second_std_deviation_end = sampleMean-(2*stdDev), sampleMean+(2*stdDev)
third_std_deviation_start, third_std_deviation_end = sampleMean-(3*stdDev), sampleMean+(3*stdDev)
print("std1", first_std_deviation_start, first_std_deviation_end)
print("std2", second_std_deviation_start, second_std_deviation_end)
print("std3", third_std_deviation_start, third_std_deviation_end)

def plotGraph(meanList):
    dataFrames = pd.read_csv("sample.csv")
    data = dataFrames["reading_time"].tolist()

    newSampleMean = statistics.mean(data)
    print("New sample mean: ", newSampleMean)

    fig = ff.create_distplot([meanList], ["Reading Time"], show_hist = False)

    fig.add_trace(go.Scatter(x=[sampleMean, sampleMean], y=[0, 0.17], mode="lines", name="SAMPLE MEAN"))
    fig.add_trace(go.Scatter(x=[newSampleMean, newSampleMean], y=[0, 0.17], mode="lines", name="NEW SAMPLE MEAN"))

    fig.add_trace(go.Scatter(x=[first_std_deviation_start, first_std_deviation_start], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1 START"))
    fig.add_trace(go.Scatter(x=[first_std_deviation_end, first_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1 END"))

    fig.add_trace(go.Scatter(x=[second_std_deviation_start, second_std_deviation_start], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2 START"))
    fig.add_trace(go.Scatter(x=[second_std_deviation_end, second_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2 END"))

    fig.add_trace(go.Scatter(x=[third_std_deviation_start, third_std_deviation_start], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 3 START"))
    fig.add_trace(go.Scatter(x=[third_std_deviation_end, third_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 3 END"))

    fig.show()

plotGraph(meanList)

#Finding the z-score using the formula
dataFrames = pd.read_csv("sample.csv")
data = dataFrames["reading_time"].tolist()
newSampleMean = statistics.mean(data)

zScore = (sampleMean - newSampleMean)/stdDev    
print("The z-score is: ", zScore)