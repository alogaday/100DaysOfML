import pickle
import numpy as np


f = open('sentiment_data.pkl', 'rb')
train_positive, train_negative, test_positive, test_negative = pickle.load(f)
f.close()

