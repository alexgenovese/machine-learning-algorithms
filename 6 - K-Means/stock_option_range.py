#!/usr/bin/python

"""
    Skeleton code for k-means clustering mini-project.
"""

import pickle
import numpy
import sys
sys.path.append("../tools/")

### load in the dict of dicts containing all the data on each person in the dataset
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )
### there's an outlier--remove it!
data_dict.pop("TOTAL", 0)


exercised_stock_options = []
for k, i in data_dict.items():
    if i['exercised_stock_options'] != 'NaN':
        exercised_stock_options.append(i['exercised_stock_options'])

exercised_stock_options = sorted(exercised_stock_options)

print("Max: ", exercised_stock_options[len(exercised_stock_options)-1])
print("Min: ", exercised_stock_options[0])