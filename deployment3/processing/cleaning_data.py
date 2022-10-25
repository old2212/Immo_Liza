#CONFIGURATION
import json
import os
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
import os
import array
from numpy import asarray
from numpy import savetxt

#FCT PREPROCESSING
def cleaning_engineering(df):
    df.drop(df.index[df['type_of_property'] == 'OTHERS'], inplace=True)

    #REPLACE NAN BY 0
    df["swimming_pool"] = df["swimming_pool"].replace(NaN, 0).astype(int)
    df["garden"] = df["garden"].replace(NaN, 0).astype(int)
    df["terrace"] = df["terrace"].replace(NaN, 0).astype(int)
    df["postal_code"] = df["postal_code"].astype(int)
    
    #TRANSLATE CATEGORIES IN NUM VALUES

        #Property_type
    map_property = {"HOUSE":1, "APARTMENT":0}
    df["type_of_property"] = df["type_of_property"].map(map_property).astype(int)

        #State_of_building
    map_state = {"GOOD":1, "TO RENOVATE":0, "JUST_RENOVATED":1, "TO REBUILD":0}
    df["state_of_the_building"] = df["state_of_the_building"].map(map_state).astype(int)

    zip_code_score = pd.read_csv('processing/zip_code_score.csv')
    df_cp = pd.DataFrame(zip_code_score)
    df = df.merge(df_cp, how='left', on='postal_code')

    #DROP FEATURES
    del df["province"]
    del df["type_of_sale"]
    del df["Unnamed: 0"]
    del df["id"]
    # del df["postal_code"]
    del df["locality"]
    del df["fully_equipped_kitchen"]
    del df["kitchen_type"]
    del df["land_surface"]
    del df["number_of_facades"]
    del df["garden_surface"]
    del df["terrace_surface"]
    del df["furnished"]
    del df["open_fire"]
    del df["region"]
    del df["subtype_of_property"]
    
    return df

#FCT CONVERT OUTPUT FILE BEFORE PREPROCESSING

def convert(item):
    df_preprocess = pd.DataFrame(item["data"], index=[0])
    
    #rename columns
    df_preprocess.rename(columns = {'facades_number':'number_of_facades', 'terrace_area':'terrace_surface', 'garden_area':'garden_surface', 'open_fire':'open_fire', 'area':'surface', 'building_state':'state_of_the_building', 'property_type':'type_of_property', 'rooms_number':'number_of_bedrooms', 'swimming_pool':'swimming_pool', 'zip_code':'postal_code'}, inplace = True)

    #add columns
    df_preprocess["province"] = np.nan
    df_preprocess["type_of_sale"] = np.nan
    df_preprocess["Unnamed: 0"] = np.nan
    df_preprocess["id"]= np.nan
    df_preprocess["locality"] = np.nan
    df_preprocess["fully_equipped_kitchen"] = np.nan
    df_preprocess["kitchen_type"] = np.nan
    df_preprocess["land_surface"] = np.nan
    df_preprocess["terrace_surface"] = np.nan
    df_preprocess["furnished"] = np.nan
    df_preprocess["open_fire"] = np.nan
    df_preprocess["region"] = np.nan
    df_preprocess["subtype_of_property"] = np.nan
    df_preprocess["price"] = 0

    #del columns (all below lines could be remove I think)
    del df_preprocess["equipped_kitchen"]
    del df_preprocess["full_address"]
    del df_preprocess["land_area"]
   

    return df_preprocess

#OUTPUT CONVERSION AND PREPROCESSING

def preprocess(item):
    convert(item)
    df = convert(item)
    df = cleaning_engineering(df)
    X_test = df.drop('price',axis= 1)
    X_test.loc[:, ['type_of_property', 'number_of_bedrooms', 'surface', 'terrace', 'garden', 'swimming_pool', 'state_of_the_building', 'postal_code_score']]
    X_test = X_test[['type_of_property', 'number_of_bedrooms', 'surface', 'terrace', 'garden', 'swimming_pool', 'state_of_the_building', 'postal_code_score']]
    X_test = X_test.loc[0].to_numpy()
    return X_test
