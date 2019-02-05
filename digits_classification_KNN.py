import pickle, gzip
import numpy as np
import cv2
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

f = gzip.open("mnist_10000.pkl.gz", "rb")

trainData, trainLabels, valData, valLabels, testData, testLabels = pickle.load(f, encoding='latin1')
f.close()

'''
image = trainData[10]
image = image.reshape((28, 28))
cv2.imshow("Image", image)
'''

for k in [1,3,5]:
    model = KNeighborsClassifier(n_neighbors = k)
    model.fit(trainData, trainLabels)
    ypred = model.predict(testData)
    print(accuracy_score(testLabels, ypred))
    print(classification_report(testLabels, ypred))
    print(confusion_matrix(testLabels, ypred))
    