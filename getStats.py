#!/usr/bin/env python3

import pandas as pd
import csv
import sys

basePath = r'/home/gchen1/Documents/micro-aevol2'
fileName = sys.argv[1] if (len(sys.argv) >= 2 ) else 'example.csv'

duration = 0
avg = 0
n = 0
max = -sys.maxsize
min = sys.maxsize

# for Macro TIME_STAMP
df = pd.read_csv(basePath + "/build/trace.csv")
durations = df.get("Duration")
n = len(durations)
for i in range(1, len(durations)): # exclude the first duration
    avg += durations[i]
    if(durations[i] > max): max = durations[i]
    if(durations[i] < min): min = durations[i]

# for pre measure
# df = pd.read_csv(basePath + "/stats/pre-measure.csv")
# colNames = ["HPC1","HPC2","HPC3","HPC4"]
# n = 30
# for i in range(0, len(colNames)): # exclude the first duration
#     avg = df[colNames[i]].mean()
#     max = df[colNames[i]].max()
#     min = df[colNames[i]].min()
#     print("avg duration: {}".format(avg))
#     print("max duration: {}".format(max))
#     print("min duration: {}".format(min))

#     try:
#         with open(basePath + r"/stats/pre-measure-" + colNames[i], 'a+') as (csvfile):
#             csvfile.write(','.join([str(avg), str(max), str(min), '\n']))
#     except OSError:
#         print("Could not open/read file, getStats.py failed")
#         sys.exit(1)
    

# # for omp timer
# file = open(basePath + "/build/execTime.txt", "r")
# for line in file:
#     if line != '\n':
#         x = float(line)
#         avg += x
#         n += 1
#         if x > max : max = x
#         if x < min : min = x
# file.close()

avg = avg/n
print("avg duration: {}".format(avg))
print("max duration: {}".format(max))
print("min duration: {}".format(min))
try:
    with open(basePath + r"/stats/" + fileName, 'a+') as (csvfile):
        csvfile.write(','.join([str(avg), str(max), str(min), '\n']))
except OSError:
    print("Could not open/read file, getStats.py failed")
    sys.exit(1)