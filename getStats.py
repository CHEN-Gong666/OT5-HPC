#!/usr/bin/env python3

import pandas as pd
import csv
import sys

basePath = r'/home/gchen1/Documents/micro-aevol2'
# colNames = ["Duration"]
df = pd.read_csv(basePath + "/build/trace.csv")
durations = df.get("Duration")
res = 0
for i in range(1, len(durations)): # exclude the first duration
    res += durations[i]
res = res/10**9
print("Total duration: {}".format(res))

try:
    with open(basePath + r"/stats/No.1-run_a_step.csv", 'a+') as (csvfile):
        csvfile.write('\n' + str(res))
except OSError:
    print("Could not open/read file, getStats.py failed")
    sys.exit(1)