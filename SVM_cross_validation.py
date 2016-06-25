#=====================================================================================
#this script will compute the K-fold cross-validation
#after SVM classification and print the score and accuracy

# Written by Mahbub Ul Alam
#=====================================================================================

#!/usr/bin/python
import numpy as np
from sklearn import cross_validation
from sklearn import datasets
from sklearn import svm

#location of processed_data.txt
#if you are using newer version of python then please use "input" instead of "raw_input" .
file_path = raw_input("Enter File location of processed_data.txt: ")

num=raw_input("Enter numbers(k) of Cross-Validation: ")

data = np.loadtxt(file_path, delimiter=",")

X = data[:, 1:]  # select all the Features
Y = data[:, 0]   # select all the target classes


clf = svm.SVC(kernel='linear', C=1)
scores = cross_validation.cross_val_score(clf, X, Y, cv=int(num))



print(scores)

print("Accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))