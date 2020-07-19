import pandas as pd
import numpy as np

gpa = pd.read_csv("GPA dataset.csv");
gpa.head(10)

req_data = gpa.iloc[:,1:]
req_data.head(10)

req_data.shape

req_data.dtypes
req_data["max. CGPA"].unique()
req_data["min. CGPA"].unique()

req_data["min. CGPA"].value_counts()

req_data.isnull().sum()

from sklearn.utils import shuffle
req_data = shuffle(req_data)

X = req_data.iloc[:,:-1].values
y = req_data["Converted GPA"].values

print(X)
print(y)

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.15,random_state=42)

print(X_train)
print(X_test)

from sklearn.ensemble import RandomForestRegressor
rand = RandomForestRegressor(n_estimators=170,criterion="mse")
rand.fit(X_train,y_train)

rand.predict([[10,5,6.895]]).round(1)

y_pred = rand.predict(X_test)

rand.score(X_test,y_test)
rand.score(X_train,y_train)

from sklearn.tree import DecisionTreeRegressor
tree = DecisionTreeRegressor(criterion="mse")
tree.fit(X_train,y_train)

tree.predict([[10,5,6.985]]).round(1)

tree.score(X_test,y_test)
tree.score(X_train,y_train)

from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train_ = sc_X.fit_transform(X_train)
X_test_ = sc_X.transform(X_test)
y_train_ = y_train.reshape(-1,1)
y_test_ = y_test.reshape(-1,1)
sc_y = StandardScaler()
y_train_ = sc_y.fit_transform(y_train_)
y_test_ = sc_y.transform(y_test_)

from sklearn.svm import SVR
svm = SVR(kernel="rbf")
svm.fit(X_train_,y_train_)

sc_y.inverse_transform(svm.predict(sc_X.transform([[10,4,7.25]]))).round(1)

y_pred = sc_y.inverse_transform(svm.predict(X_test_)).round(1)
sc_y.inverse_transform(y_test_)

svm.score(X_test_,y_test_)
svm.score(X_train_,y_train_)

from sklearn.linear_model import LinearRegression
lr = LinearRegression()
lr.fit(X_train,y_train)

lr.predict([[10,5,7.35]]).round(1)

lr.score(X_train,y_train)
lr.score(X_test,y_test)

import pickle
file = open("german_gpa.pkl","wb")
pickle.dump(rand,file)