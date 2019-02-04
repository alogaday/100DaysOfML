from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

dataset = load_iris()
X = dataset.data
y = dataset.target

ss = StandardScaler()
X_stdzied = ss.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X_stdzied, y, test_size = 0.33, random_state = 12)

model = KNeighborsClassifier(n_neighbors = 5, metric = "minkowski", p =2)
# p=2 for euclidian distance

model.fit(X_train, y_train)
y_pred = model.predict(X_test)

print(accuracy_score(y_test, y_pred))