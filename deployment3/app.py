#config
import json
import time
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
from fastapi import FastAPI
from os import path
import sys
import uvicorn
from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel


#import functions from other repository in deployment
from predict.prediction import predict

class Input(BaseModel):
    area: int
    property_type: str = None
    rooms_number: int
    zip_code : int
    land_area : Optional[int] = None
    garden : Optional[bool] = None
    garden_area : Optional[int] = None
    equipped_kitchen : Optional[bool] = None
    full_address : Optional[str] = None
    swimming_pool : Optional[bool] = None
    furnished : Optional[bool] = None
    open_fire : Optional[bool] = None
    terrace : Optional[bool] = None
    terrace_area : Optional[int] = None
    facades_number : Optional[int] = None
    building_state : Optional[str] = None

class Input2(BaseModel):
    data:Input


immo_app = FastAPI()

@immo_app.get("/")
async def root():
    return {"message": "Hello World"}

@immo_app.post("/predict/")
async def new_property(item:Input2):
    price = predict(item.dict())
    return {"prediction:": price}
