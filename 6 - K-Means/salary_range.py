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


salary_arr = []
for k, i in data_dict.items():
    if i['salary'] != 'NaN':
        salary_arr.append(i['salary'])

salary_arr = sorted(salary_arr)

print "Max: ", salary_arr[len(salary_arr)-1]
print "Min: ", salary_arr[0]