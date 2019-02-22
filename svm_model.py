# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 11:20:46 2019

@author: sainath.gaddam
"""

import numpy as np
X = np.array([[-1,-1],[-2,-1],[1,1],[2,1]])
y = np.array([0,0,1,1])

from sklearn.svm import SVC

clf = SVC()
clf.fit(X,y)


clf.predict([[-0.8, -1]])