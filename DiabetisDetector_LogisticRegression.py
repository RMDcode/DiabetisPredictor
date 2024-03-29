import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from warnings import simplefilter

simplefilter(action='ignore',category=FutureWarning)

seperator = "-" * 50

print("---Marvellous Infosystems---")

print("---Diabetes predictor using Logistic Regression---")

diabetes = pd.read_csv('diabetes.csv')

print(seperator)
print("Columns of Dataset")
print(diabetes.columns)
print(seperator)


print("First 5 records of dataset")
print(diabetes.head())
print(seperator)

print("Dimension of diabetes data : {}".format(diabetes.shape))
print(seperator)

X_train, X_test, y_train, y_test=train_test_split(diabetes.loc[:,diabetes.columns!='Outcome'], diabetes['Outcome'], stratify=diabetes['Outcome'], random_state=66)

logreg = LogisticRegression(max_iter=1000).fit(X_train, y_train)

print("Training set accuracy : {:.3f}".format(logreg.score(X_train,y_train)))
print(seperator)
print("Test set accuracy : {:.3f}".format(logreg.score(X_test,y_test)))
print(seperator)

logreg001= LogisticRegression(C=0.01, max_iter=1000).fit(X_train,y_train)

print(seperator)
print("Training set accuracy: {:.3f}".format(logreg001.score(X_train,y_train)))
print(seperator)
print("Test set accuracy: {:.3f}".format(logreg001.score(X_test,y_test)))
print(seperator)

