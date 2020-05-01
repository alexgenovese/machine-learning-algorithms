#!/usr/bin/python


"""
    Starter code for the evaluation mini-project.
    Start by copying your trained/tested POI identifier from
    that which you built in the validation mini-project.

    This is the second step toward building your POI identifier!

    Start by loading/formatting the data...
"""

import pickle
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "r") )

### add more features to features_list!
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)

from sklearn import tree

dt = tree.DecisionTreeClassifier() # overfitting tha data on all dataset
dt.fit(features, labels)
dt.predict(features)

# Yet another case where testing on the training data
# would make you think you were doing amazingly well, but as you already know,
# that's exactly what holdout test data is for...
_score = dt.score(features, labels)
print("SCORE: ", _score)

from sklearn.cross_validation import train_test_split
# features_train, features_test, labels_train, labels_test
X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.3, random_state=42)

dt.fit(X_train, y_train)
predicted = dt.predict(X_test, y_test)

_score = dt.score(X_test, y_test)
print("SCORE: ", _score)

#----------------------------------------------------------
#
# Number of POIs in Test Set
# How many POIs are predicted for the test set for your POI identifier?
# (Note that we said test set! We are not looking for the number of POIs in the whole dataset.)
#

# step 2 : look at result type and contents.
import numpy as np

pois_predicted_in_test_data = 0
for k in np.array(y_test):
    if k == 1:
        pois_predicted_in_test_data += 1

print("POIs predicted for the test set: ", pois_predicted_in_test_data)

#----------------------------------------------------------
#
# Number of People in test set
#
print(len(y_test))

#----------------------------------------------------------
#
# Accuracy
#


#----------------------------------------------------------
#
# Number of true positive:
#

of_true_positives = [(x,y) for x, y in zip(predicted, y_test) if x == y and x == 1.0]
print("True positives on the Overfitted model: ", len(of_true_positives))


from sklearn.metrics import precision_score
p_score = precision_score( y_test, predicted )

print("Precision score: ", p_score)


from sklearn.metrics import recall_score
r_score = recall_score( y_test, predicted )

print("Recall score: ", p_score)