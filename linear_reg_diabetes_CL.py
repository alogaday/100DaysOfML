import numpy as np
from sklearn import datasets, linear_model, metrics
from sklearn.model_selection import train_test_split


diabetes = datasets.load_diabetes()

diabetes_X = diabetes.data # matrix of dimensions 442x10
 
# Split the data into training/testing sets
diabetes_X_train = diabetes_X[:-20]
diabetes_X_test = diabetes_X[-20:]
 
# Split the targets into training/testing sets
diabetes_y_train = diabetes.target[:-20]
diabetes_y_test = diabetes.target[-20:]



model = linear_model.LinearRegression()
model.fit(diabetes_X_train, diabetes_y_train)

y_pred = model.predict(diabetes_X_test)

# the coefficients

print("Coefficients ", model.coef_)


#accuracy for regression

#https://scikit-learn.org/stable/modules/classes.html#regression-metrics

mean_sq_error = metrics.mean_squared_error(diabetes_y_test, y_pred)
print("mean squared error is ", mean_sq_error)