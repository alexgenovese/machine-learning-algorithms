#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit
from operator import itemgetter

### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )
features = ["salary", "bonus"]
data = featureFormat(data_dict, features)

data = data.tolist()
salary_data=[data[i][0] for i in range(0,len(data))]
max_label=[i for i,x in enumerate(salary_data) if x==max(salary_data)]

data.pop( max_label[0] ) # removed the outliers

""""
best_bonus_ever = []
for key, i in data_dict.items():
    if i['bonus'] > 3000000 and i['bonus'] != 'NaN':
        best_bonus_ever.append([key, i['bonus'], i['salary']])


best_bonus_ever.sort(key= itemgetter(1))
print best_bonus_ever
""""


for point in data:
    salary = point[0]
    bonus = point[1]
    matplotlib.pyplot.scatter( salary, bonus )

matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
matplotlib.pyplot.show()