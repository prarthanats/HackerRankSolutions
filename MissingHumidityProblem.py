# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 12:29:08 2019
@author: Prarthana
Predicting the Missing Humidity Values
"""

import datetime
import numpy as np
from sklearn.linear_model import LinearRegression

def predictMiss(startDate, endDate, knownTimestamps, humidity, timestamps):
    x = [int(abs((datetime.datetime.utcfromtimestamp(0) - datetime.datetime.strptime(item,"%Y-%m-%d %H:%M")).total_seconds())) for item in knownTimestamps]
    y = humidity

    lm = LinearRegression()
    lm.fit(np.array(x).reshape(-1,1),y)

    z = [int(abs((datetime.datetime.utcfromtimestamp(0) - datetime.datetime.strptime(item,"%Y-%m-%d %H:%M")).total_seconds())) for item in timestamps]
    return lm.predict(np.array(z).reshape(-1,1))

answer = predictMis(startDate, endDate, knownTimestamps, humidity, timestamps)
print(answer)