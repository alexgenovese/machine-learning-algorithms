#!/usr/bin/python


"""
    Starter code for the validation mini-project.
    The first step toward building your POI identifier!

    Start by loading/formatting the data

    After that, it's not our code anymore--it's yours!
"""

import pickle
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "r") )

### first element is our labels, any added elements are predictor
### features. Keep this the same for the mini-project, but you'll
### have a different feature list when you do the final project.
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

X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.3, random_state=42)

dt.fit(X_train, y_train)
dt.predict(X_test, y_test)

_score = dt.score(X_test, y_test)
print("SCORE: ", _score)