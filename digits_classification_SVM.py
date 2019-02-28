import pickle, gzip
import numpy as np
import cv2
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

f = gzip.open("mnist_1000.pkl.gz", "rb")

trainData, trainLabels, valData, valLabels, testData, testLabels = pickle.load(f, encoding='latin1')
f.close()

'''
image = trainData[10]
image = image.reshape((28, 28))
cv2.imshow("Image", image)
'''


from sklearn.svm import SVC

clf = SVC()
clf.fit(trainData,trainLabels)

y_pred = clf.predict(testData)

print(accuracy_score(testLabels,y_pred))

