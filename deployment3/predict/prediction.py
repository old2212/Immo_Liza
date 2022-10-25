#config

import json
import time
import seaborn as sb
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats
from numpy import NaN
from sklearn.utils import shuffle
from sklearn.model_selection  import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error
from sklearn import preprocessing
from sklearn.preprocessing import OneHotEncoder
from sklearn import metrics
from sklearn.neighbors import KNeighborsClassifier as KNN
from sklearn.datasets import load_iris
import pickle
from numpy import loadtxt
from numpy import savetxt
import array
import sys
from os import path
#import functions from other repository in deployment
from processing.cleaning_data import preprocess

# Load the Model back from file
def predict(item) :
    #Load the saved model
    X_test = preprocess(item)
    Pkl_Filename = "model/Pickle_RL_Model.pkl"
    with open(Pkl_Filename, 'rb') as file:  
        Pickled_LR_Model = pickle.load(file)
    #run the model with the output_data
    Ypredict = Pickled_LR_Model.predict([X_test])
    #save my result of predicted_price
    return Ypredict[0]