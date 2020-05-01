#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

# Lesson 6.15
no_entries_poi_1 = 0
for key, i in enron_data.items():
    if enron_data[key]['poi'] == 1:
        no_entries_poi_1 += 1

print("Number of entries of POI == 1: ", no_entries_poi_1)

# Lesson 6.16
poi_name_record = open("../final_project/poi_names.txt").read().split("\n")
poi_name_total = [record for record in poi_name_record if "(y)" in record or "(n)" in record]
print("Total number of POIs: ", len(poi_name_total))

# Lesson 6.18
for key_person_name, i in enron_data.items():
    if key_person_name.startswith('PRENTICE'):
        # print key_person_name, i
        print(['total_stock_value'])


# Lesson 6.19
for key_person_name, i in enron_data.items():
    if key_person_name.startswith('COLWELL'):
        print(['from_this_person_to_poi'])


# Lesson 6.20
for key_person_name, i in enron_data.items():
    if key_person_name.startswith('SKILLING'):
        print(['exercised_stock_options'])


# Lesson 6.25 - who has most total_payments?
salary_sort = []
for key_person_name, i in enron_data.items():
    if key_person_name.startswith('LAY'):
        print("LAY SALARY: ", enron_data[key_person_name]['total_payments'])
        salary_sort.append(enron_data[key_person_name]['total_payments'])
    if key_person_name.startswith('SKILLING'):
        print("SKILLING SALARY: ", enron_data[key_person_name]['total_payments'])
        salary_sort.append(enron_data[key_person_name]['total_payments'])
    if key_person_name.startswith('FASTOW'):
        print("FASTOW SALARY: ", enron_data[key_person_name]['total_payments'])
        salary_sort.append(enron_data[key_person_name]['total_payments'])

salary_sort.sort()
print(salary_sort)

# Lesson 6.27
salary_known = 0
for key_person_name, i in enron_data.items():
    if enron_data[key_person_name]['salary'] != 'NaN':
        # print key_person_name, " salary: ", enron_data[key_person_name]['salary']
        salary_known += 1

print("How many folks in this dataset have a quantified salary?", salary_known)


# Lesson 6.27
email_known = 0
for key_person_name, i in enron_data.items():
    if i['email_address'] != 'NaN':
        # print key_person_name, " salary: ", enron_data[key_person_name]['salary']
        email_known += 1

print("How many folks in this dataset have a known email?", email_known)


# Lesson 6.29
nan_total_payments = 0
for key_person_name, i in enron_data.items():
    if i['total_payments'] == 'NaN':
        nan_total_payments += 1

print("How many people have NaN for their total payments?", nan_total_payments, len(enron_data), 100*nan_total_payments/len(enron_data), "%")


# Lesson 6.30
poi_nan_total_payments = 0
poi = 0
for key_person_name, i in enron_data.items():
    if i['poi']:
        print(['poi'])
        poi += 1

    if i['total_payments'] == 'NaN':
        if i['poi'] == 'NaN':
            poi_nan_total_payments += 1

print("How many POIs in the E+F dataset have NaN for their total payments?", poi_nan_total_payments, len(enron_data), 100*poi_nan_total_payments/len(enron_data), "% ", poi)