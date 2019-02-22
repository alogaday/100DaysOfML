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

acc_score = []

#for k in [1, 3, 5, 9, 15, 25]:
model = KNeighborsClassifier(n_neighbors = 3)
model.fit(trainData, trainLabels)
ypred = model.predict(testData)
acc_score.append(accuracy_score(testLabels, ypred))
    
print(accuracy_score(testLabels, ypred))
print(classification_report(testLabels, ypred))
print(confusion_matrix(testLabels, ypred))
    
