from sklearn.model_selection import train_test_split

# Droping the target and species since we only need the measurements
X = iris.drop(['variety'], axis=1)

# converting into numpy array and assigning petal length and petal width
X = X.to_numpy()
y = iris['variety']

# Splitting into train and test
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.5, random_state=42)

from sklearn.linear_model import LogisticRegression

log_reg = LogisticRegression()
log_reg.fit(X_train,y_train)

log_reg.predict(X_test)

import joblib
# now you can save it to a file
joblib.dump(log_reg, 'iris.pkl') 
