import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import numpy as np

data = pd.read_csv("diabetes.csv")
data.head()

X = data.iloc[:, 0:8]
y = data.iloc[:,8]

X_train, X_test, y_train, y_test= train_test_split(X,y,test_size = 0.33)

mean = np.mean(X_train, axis = 0)
stds = np.std(X_train, axis = 0)

X_train_nrm = (X_train - mean)/stds
X_test_nrm = (X_test - mean)/stds

model = LogisticRegression()
model.fit(X_train_nrm, y_train)
y_pred = model.predict(X_test_nrm)
y_pred_prob = model.predict_proba(X_test_nrm)

print(accuracy_score(y_test, y_pred))

# interpreting the model

coeff = list(model.coef_[0])
labels = list(X.columns)

features = pd.DataFrame()
features["Features"]  = labels
features["Importance"] = coeff

features.sort_values(by = ["Importance"], ascending=True, inplace=True)

features["Positive"] = features["Importance"] > 0

features.Importance.plot(kind='barh', figsize=(11, 6),color = features.Positive.map({True: 'blue', False: 'red'}))
