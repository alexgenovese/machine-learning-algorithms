#!/usr/bin/python

import pickle
import numpy
numpy.random.seed(42)


### The words (features) and authors (labels), already largely processed.
### These files should have been created from the previous (Lesson 10)
### mini-project.

# words_file = "./word_data_overfit.pkl"
# authors_file = "./email_authors_overfit.pkl"
words_file = "../11 - Text Learning/your_word_data.pkl"
authors_file = "../11 - Text Learning/your_email_authors.pkl"
word_data = pickle.load( open(words_file, "r"))
authors = pickle.load( open(authors_file, "r") )



### test_size is the percentage of events assigned to the test set (the
### remainder go into training)
### feature matrices changed to dense representations for compatibility with
### classifier functions in versions 0.15.2 and earlier
from sklearn import model_selection
features_train, features_test, labels_train, labels_test = model_selection.train_test_split(word_data, authors, test_size=0.1, random_state=42)

from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer = TfidfVectorizer(sublinear_tf=True, max_df=0.5,
                             stop_words='english')
features_train = vectorizer.fit_transform(features_train)
features_test  = vectorizer.transform(features_test).toarray()

name = vectorizer.get_feature_names()

### a classic way to overfit is to use a small number
### of data points and a large number of features;
### train on only 150 events to put ourselves in this regime
features_train = features_train[:150].toarray()
labels_train   = labels_train[:150]

from sklearn import tree

clf = tree.DecisionTreeClassifier()
clf.fit(features_train, labels_train)
pred = clf.predict(features_train)

score = clf.score(features_test, labels_test)

# the test performance has an accuracy much higher than it is expected to be
# if we are overfitting, then the test performance should be relatively low
print("Score on TEST in Decision Tree overfitting: ", score)


# What s the importance of the most important feature?
# What is the number of this feature?
most_important_word_value = 0
index = 0
for i in clf.feature_importances_:
    if i > 0.2:
        most_important_word_value = i
        index_most_important_word = index

    index += 1

print(most_important_word_value, index_most_important_word)
print(name[index_most_important_word])