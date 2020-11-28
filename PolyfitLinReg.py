# -*- coding: utf-8 -*-
"""
@author: Paul


Resources:
https://scipy-cookbook.readthedocs.io/items/LinearRegression.html

run these installationsfollowing before running the code:

pip install pandas_market_calendars
"""

from scipy import linspace, polyval, polyfit, sqrt, stats, randn
from matplotlib.pyplot import plot, title, show, legend, figure
import numpy as np
import pandas as pd
import pandas_market_calendars as mcal
from alpha_vantage.timeseries import TimeSeries
from datetime import time



api_key = '8FIYTT49ZEZT2GV5'
ts = TimeSeries(key=api_key, output_format='pandas')
data, meta_data = ts.get_daily(symbol='SPY', outputsize = 'full')

data = data.reset_index()
data['date'] = data['date'].dt.strftime('%Y%m%d')
data['date'] = data['date'].values.astype(int)

X = np.c_[data['date']]
#print(X)
Y = np.c_[data['4. close']]
#print(Y)

# erasing the squared bracket of every element
X = [i[0] for i in X]
#print(x)
Y = [i[0] for i in Y]
#print(y)

#Reversing the order of X and Y
x= X[::-1]
#print(x)
last_day = len(x)-1
#print(x[last_day])
y = Y[::-1]
#print(y)
#print(y[last_day])

# list of th day opening date since 1999-11-01 which very starting our date. 
# instead of YYYYMMDD for linear regression 
th_day = list(range(0,last_day+1))
#print(th_day)
#print(len(th_day))
#print(len(x))

'''
#plotting our pure x and y from data
figure()
title('th_day since 19991101 closing prices')
plot(th_day, y)
'''

'''
figure()
title('YYYYMMDD closing prices')
plot(x, y)
'''

# 1th order of poly which is linear: y (x) = p[0]x + p[1].
# p = an array of poly coefficients
p = np.polyfit(th_day, y, 1)
#print(p[0])
#print(p[1])

#linear regression y(th_day) function
lr_y = np.polyval(p, th_day)


figure()
title('th_day since 19991101 closing prices: Polyfit Linear regression')
plot(th_day, y)
plot(th_day, lr_y)
legend(['original', 'linear regression'])

#calculating future date th_day opening since 1999-11-01
nyse = mcal.get_calendar('NYSE')
def YYYY_MM_DD_to_th_day(YMD):
    early = nyse.schedule(start_date='1999-11-01', end_date=YMD)
    return len(early)-1

d = YYYY_MM_DD_to_th_day('2020-11-27')
#print(d)
d_lr_prediction_price =  np.polyval(p, d)
#print("linear_regression prediction closing price for 2020-11-27:", d_lr_prediction_price)

#print("actualy closing price for 2020-11-27:", y[d])

d = YYYY_MM_DD_to_th_day('2020-12-27')

d_lr_prediction_price =  np.polyval(p, d)
#print("linear_regression prediction closing price for 2020-12-27:", d_lr_prediction_price)

'''
# root-mean-square error calculation
lr_y = np.polyval(p, th_day)
#print(lr_y)
lr_error = lr_y-y
#print(lr_error)
lr_error_squared = np.power(lr_error, 2)
#print(lr_error_squared)
lr_error_squared_sum = sum(lr_error_squared)
#print(lr_error_squared_sum)
#print(lr_error_squared_sum/len(y))
lr_rmse =  np.lib.scimath.sqrt(lr_error_squared_sum/len(y))
print('root mean square error:', lr_rmse)
'''

#rmse function
def rmse(true_y, predicted_y, time):
    error = true_y-predicted_y
    error_squared = np.power(error, 2)
    error_squared_sum = sum(error_squared)
    rmse =  np.lib.scimath.sqrt(error_squared_sum/len(true_y))
    return rmse

#print('root mean square error for linear regression (polyfit)', rmse(y, lr_y, th_day))


###################################
#testing with bigger polynomial
###################################

##########################
# 2nd degree of polynomial
##########################
p2 = np.polyfit(th_day, y, 2)
#print(p2)
p2_y = np.polyval(p2, th_day)

figure()
title('th_day since 19991101 closing prices: 2nd degree regression')
plot(th_day, y)
plot(th_day, lr_y)
plot(th_day, p2_y)
legend(['original', 'linear regression', '2nd degree regression'])

#print('root mean square error for 2nd degree regression:', rmse(y, p2_y, th_day))
#almost twice better

d = YYYY_MM_DD_to_th_day('2020-11-27')
#print(d)
d_p2_prediction_price =  np.polyval(p2, d)
#print("2nd degree polynomial regression closing price for 2020-11-27:", d_p2_prediction_price)

#print("actualy closing price for 2020-11-27:", y[d])

d = YYYY_MM_DD_to_th_day('2020-12-27')

d_p2_prediction_price =  np.polyval(p2, d)
#print("2nd degree polynomial regression closing price for 2020-12-27:", d_p2_prediction_price)


##########################
# 3rd degree of polynomial
##########################

p3 = np.polyfit(th_day, y, 3)
#print(p3)
p3_y = np.polyval(p3, th_day)

figure()
title('th_day since 19991101 closing prices: 3rd degree regression')
plot(th_day, y)
plot(th_day, lr_y)
plot(th_day, p2_y)
plot(th_day, p3_y)
legend(['original', 'linear regression', '2nd degree regression', '3rd degree regression'])

#print('root mean square error for 3rd degree regression:', rmse(y, p3_y, th_day))

d = YYYY_MM_DD_to_th_day('2020-11-27')
#print(d)
d_p3_prediction_price =  np.polyval(p3, d)
#print("3rd degree polynomial regression closing price for 2020-11-27:", d_p3_prediction_price)

#print("actual closing price for 2020-11-27:", y[d])

d = YYYY_MM_DD_to_th_day('2020-12-27')

d_p3_prediction_price =  np.polyval(p3, d)
#print("3rd degree polynomial regression closing price for 2020-12-27:", d_p3_prediction_price)

# th degree polynomial degree testing
def th_degree_polynomial_testing(th_degree, x, y):
    p_th = np.polyfit(x, y, th_degree)
    #print(p_th)
    p_th_y = np.polyval(p_th, x)
    
    figure()
    title('th_day since 19991101 closing prices {}th degree regression'.format(th_degree))
    plot(th_day, y)
    plot(th_day, p2_y)
    plot(th_day, p_th_y)    
    legend(['original', '2nd degree regression','{}th degree regression'.format(th_degree)])
    print('root mean square error for {}th degree regression: {}'.format(th_degree, rmse(y, p_th_y, th_day)))
    return p_th

#th_degree_polynomial_testing(4, th_day, y)
#th_degree_polynomial_testing(5, th_day, y)
#th_degree_polynomial_testing(10, th_day, y)
#th_degree_polynomial_testing(20, th_day, y)
#th_degree_polynomial_testing(30, th_day, y)
#th_degree_polynomial_testing(40, th_day, y)
#th_degree_polynomial_testing(50, th_day, y)

p82 = th_degree_polynomial_testing(82, th_day, y)
d = YYYY_MM_DD_to_th_day('2020-11-27')
#print(d)
d_p82_prediction_price =  np.polyval(p82, d)
print("82th degree polynomial regression closing price for 2020-11-27:", d_p82_prediction_price)

print("actual closing price for 2020-11-27:", y[d])

d = YYYY_MM_DD_to_th_day('2020-12-27')

d_p82_prediction_price =  np.polyval(p3, d)
print("82th degree polynomial regression closing price for 2020-12-27:", d_p82_prediction_price)