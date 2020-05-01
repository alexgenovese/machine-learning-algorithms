#!/usr/bin/python

"""
    Skeleton code for k-means clustering mini-project.
"""


# Lesson 10.16

import pickle
from sklearn.preprocessing import MinMaxScaler
import sys
sys.path.append("../tools/")

### load in the dict of dicts containing all the data on each person in the dataset
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )
### there's an outlier--remove it!
data_dict.pop("TOTAL", 0)


salary_arr = []
for k, i in data_dict.items():
    if i['salary'] != 'NaN':
        salary_arr.append([float(i['salary'])]) # MinMaxScaler wants float number and 2D Array !!!

# Add max value to 200.000 - for the example
salary_arr.append([float(200000)])
salary_arr = sorted(salary_arr)

scaler = MinMaxScaler()
rescaled_salary = scaler.fit_transform(salary_arr)

print rescaled_salary