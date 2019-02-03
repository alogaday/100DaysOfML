import numpy as np
from sklearn import datasets, linear_model, metrics
from sklearn.model_selection import train_test_split


diabetes = datasets.load_diabetes()
diabetes_X = diabetes.data
print(diabetes_X.shape)

diabetes_y = diabetes.target
print(diabetes_y.shape)

X_train, X_test, y_train, y_test= train_test_split(diabetes_X, diabetes_y, test_size = 0.01)

model = linear_model.LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

# the coefficients

print("Coefficients ", model.coef_)


#accuracy for regression

#https://scikit-learn.org/stable/modules/classes.html#regression-metrics

mean_sq_error = metrics.mean_squared_error(y_test, y_pred)
print("mean squared error is ", mean_sq_error)