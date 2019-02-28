from sklearn.datasets import load_iris
from sklearn.naive_bayes import GaussianNB
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

data = load_iris()

model = GaussianNB()

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size =0.33, random_state = 42)

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print(accuracy_score(y_test, y_pred))
