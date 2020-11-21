import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import sklearn.linear_model
import scipy.stats as stats
from alpha_vantage.timeseries import TimeSeries
api_key = '8FIYTT49ZEZT2GV5'

ts = TimeSeries(key=api_key, output_format='pandas')
data, meta_data = ts.get_daily(symbol='SPY', outputsize = 'full')

data = data.reset_index()
data['date'] = data['date'].dt.strftime('%Y%m%d')
data['date'] = data['date'].values.astype(int)

X = np.c_[data['date']]
Y = np.c_[data['4. close']]

model = sklearn.linear_model.LinearRegression()
model.fit(X, Y)
std = np.std(Y)

testdate = [[20211218]]
testprediction = model.predict(testdate)
testprice = testprediction[0] + (-2.5 * std)
zscore = float((testprice - testprediction[0]) / std)

probability = 0
cdf = stats.norm.cdf(zscore)

if(cdf <= .5):
	probability = cdf
elif(cdf >= .5):
	probability = 1-cdf

print(testprediction)

'''
https://www.youtube.com/watch?v=EShuLfSxpsI

We need to change the model, the linear model is way too off.

''' 