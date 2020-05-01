#!/usr/bin/python

"""
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:
    Sara has label 0
    Chris has label 1
"""

import sys
from sklearn import svm
from time import time

sys.path.append("../tools/")
from email_preprocess import preprocess

### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()

# One way to speed up an algorithm is to train it on a smaller training dataset.
# The tradeoff is that the accuracy almost always goes down when you do this.
# Let s explore this more concretely: add in the following two lines immediately before training your classifier
# features_train = features_train[:len(features_train)/100]
# labels_train = labels_train[:len(labels_train)/100]
# These lines effectively slice the training dataset down to 1% of its original size,
# tossing out 99% of the training data. You can leave all other code unchanged. What s the accuracy now?

clf = svm.SVC(kernel='rbf', gamma=1, C=10.0)
t0 = time()
clf.fit(features_train, labels_train)
print "training time: ", round(time() - t0, 3), " s"

t1 = time()
predict = clf.predict(features_test)
print "testing time: ", round(time() - t1, 3), " s"

t2 = time()
score = clf.score(features_test, labels_test)
print "scoring time: ", round(time() - t2, 3), " s", "scoring: ", score