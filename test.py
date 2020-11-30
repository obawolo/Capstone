import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import sklearn.linear_model
import scipy.stats as stats
import pandas_market_calendars as mcal
from alpha_vantage.timeseries import TimeSeries
api_key = '8FIYTT49ZEZT2GV5'

ts = TimeSeries(key=api_key, output_format='pandas')
data, meta_data = ts.get_daily(symbol='SPY', outputsize = 'full')

data = data.reset_index()
data['date'] = data['date'].dt.strftime('%Y%m%d')
data['date'] = data['date'].values.astype(int)

X = np.c_[data['date']]
Y = np.c_[data['4. close']]
X = [i[0] for i in X]
Y = [i[0] for i in Y]

X = X[::-1] #REVERSING ORDER
Y = Y[::-1] #REVERSING ORDER
last_day = len(X) - 1
th_day = list(range(0,last_day+1))

def YYYY_MM_DD_to_th_day(YMD):
    early = nyse.schedule(start_date='1999-11-01', end_date=YMD)
    return len(early)-1

model = np.polyfit(X, Y, 4)
std = np.std(Y)

testdate = [[20210101]] 
testprediction = np.polyval(model, testdate)
testprice = testprediction[0] + (1 * std)
zscore = float((testprice - testprediction[0]) / std)

probability = 0
cdf = stats.norm.cdf(zscore)

if(cdf <= .5):
	probability = cdf
elif(cdf >= .5):
	probability = 1-cdf


print(testprediction)

#NEW CODE STARTING BELOW
#OK, .01 std tests
#get the best trade per day
#choose...idk

'''
shortPrices = 0
longPrices = 0

currentPrice = Y[0]
reward = longPrices - currentPrice
risk = currentPrice - shortPrices

print(reward)
print(risk) 
'''




#OPTIMIZATION TESTS

#ULTRA SHORT TERM (original: 20211218), TODAY : 360
#1st Degree : 255 in a week, 255 in a month, 263 in 6 months
#2nd Degree : 320 in a week, 320 in a month, 347 in 6 months
#3rd Degree : 325 in a week, 325 in a month, 356 in 6 months
#4th Degree : 323 in a week, 323 in a month, 351 in 6 months
#5th Degree : 323 in a week, 323 in a month, 351 in 6 months

#SHORT TERM
#1st Degree : 264 in 2021, 273 in 2022
#2nd Degree : 349 in 2021, 381 in 2022
#3rd Degree : 359 in 2021, 396 in 2022
#4th Degree : 353 in 2021, 385 in 2022
#5th Degree : 353 in 2021, 385 in 2022

#ULTRA LONG TERM (assuming downturns every 10 years)
#1st Degree : 344 in 2030, 434 in 2040
#2nd Degree : 704 in 2030, 1282 in 2040
#3rd Degree : 804 in 2030, 1652 in 2040
#4th Degree : 649 in 2030, 759 in 2040
#5th Degree : 648 in 2030, 745 in 2040

#COMPARISON TO EXTERNAL PREDICTIONS (11/26/25, $486)
#1st Degree: 300
#2nd Degree: 487
#3rd Degree: 523
#4th Degree: 484
#5th Degree: 484

#BEST RESULT : 4th Degree

#ACCURACY TEST
#Today: 0.5Z
#March Low : -1.5Z
#February High : 0.27Z
#2009 Low : -0.71Z
#2007 High : 0.66Z