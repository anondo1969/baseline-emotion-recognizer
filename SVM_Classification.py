#=====================================================================================
#this script will compute the SVM classification and print the Accuracy score

# Written by Mahbub Ul Alam
#=====================================================================================

import numpy as np
from sklearn import cross_validation
from sklearn import svm
from sklearn.metrics import accuracy_score

#if you are using newer version of python then please use "input" instead of "raw_input" .
#location of training_data.txt
training_data_file_path = raw_input("Enter training data location: ")
#location of development_data.txt
test_data_file_path = raw_input("Enter test data location: ")

training_data = np.loadtxt(training_data_file_path, delimiter=",")

X = training_data[:, 1:]  # select all the Features in training data
Y = training_data[:, 0]   # select all the target classes in training data

test_data = np.loadtxt(test_data_file_path, delimiter=",")

x_test = test_data[:, 1:]  # select all the Features in test data
y_true = test_data[:, 0]   # select all the target classes in test data

clf = svm.SVC(decision_function_shape='ovo')
clf.fit(X, Y)

y_pred = clf.predict(x_test)

score = accuracy_score(y_true, y_pred)

print("Accuracy: ")
print(score)