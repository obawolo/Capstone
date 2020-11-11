#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 09:14:43 2020

@author: kosi
"""

import pandas as pd
from alpha_vantage.timeseries import TimeSeries
import time
api_key = '8FIYTT49ZEZT2GV5'

ts = TimeSeries(key=api_key, output_format='pandas')
data, meta_data = ts.get_intraday(symbol='SPY', interval = '1min', outputsize = 'full')
print (data)

close_data = data['4. close']
percentage_change = close_data.pct_change()
print(percentage_change)

last_change = percentage_change[-1]

if abs(last_change) > 0.0004:
    print("SPY Alert:" + str(last_change))

import matplotlib.pyplot as plt
import alpha_vantage as sns
sns.pairplot(sales, x_vars=['Price'],y_vars='time variables')
plt.show()
#Creating X and Y
x = sales['Time variables’]
y = sales['Price’]
#plot data to see if it can be linearly fitted
plt.scatter(X_scaled_values,Y_scaled_values, alpha = 0.7)
from sklearn.model_selection 
import train_test_split
from sklearn.model_selection import train_test_split
x_train, y_train, X_test, y_test = train_test_split(x, y, train_size=jj, test_size=jj,random_state=jj
#take a look at the train dataset
x_train
y_train 
# Create linear regression object
regr = linear_model.LinearRegression()
regr.fit(X_train, Y_train)
from sklearn.linear_model import SGDRegressor
predictions = regr.predict(X_test)
from sklearn.metrics import classification_report
print(classification_report(y_test,predictions))
plt.scatter(X_test, Y_test,  color)
plt.title(‘Test Data’)
plt.xlabel(‘time Variables)
plt.ylabel(‘Price’)
plt.xticks(())
plt.yticks(())
plt.show()
plt.plot(X_test, regr.predict(X_test), color=’red’,linewidth=3)
#do standard deviation.


