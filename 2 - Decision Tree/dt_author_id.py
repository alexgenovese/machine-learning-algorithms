#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 3 (decision tree) mini-project.

    Use a Decision Tree to identify emails from the Enron corpus by author:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess
from sklearn.tree import DecisionTreeClassifier


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels

features_train, features_test, labels_train, labels_test = preprocess()

# features_train = features_train[:len(features_train)/100]
# labels_train = labels_train[:len(labels_train)/100]

cls = DecisionTreeClassifier(min_samples_split=40)

t0 = time()
cls.fit(features_train, labels_train)
print "training time: ", round(time() - t0, 3), " s"

t1=time()
cls.predict(features_test)
print "testing time: ", round(time() - t1, 3), " s"

t2=time()
_score = cls.score(features_test, labels_test)
print "score time: ", round(time() - t2, 3), " s", "SCORE: ", _score

# What's the number of features in your data?
print len(features_train[0])