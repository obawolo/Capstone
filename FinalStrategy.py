import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import sklearn.linear_model
import scipy.stats as stats
import pandas_market_calendars as mcal
from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.techindicators import TechIndicators
api_key = '8FIYTT49ZEZT2GV5'

ts = TimeSeries(key=api_key, output_format='pandas')
data, meta_data = ts.get_daily(symbol='SPY', outputsize = 'full')
nyse = mcal.get_calendar('NYSE')

def dateToIndex(YMD):
    count = nyse.schedule(start_date='1999-11-01', end_date=YMD)
    return len(count)-1

def probability(price, prediction, dev):
	probability = 0
	zscore = float((price - prediction) / dev)
	cdf = stats.norm.cdf(zscore)
	if(cdf <= .5):
		probability = cdf
	elif(cdf >= .5):
		probability = 1-cdf
	return probability

data = data.reset_index()
data['date'] = data['date'].dt.strftime('%Y-%m-%d')
data['index'] = list(reversed(range(0, len(data))))

X = np.c_[data['index']]
Y = np.c_[data['4. close']]
X = [x[0] for x in X]
Y = [x[0] for x in Y]

model = np.polyfit(X, Y, 3)
std = np.std(Y)
todayDate = X[0]
currentPrice = Y[0]
std = np.std(Y)
dateTestBench = [3, 5, 7, 11, 13, 17, 19]

#temporary, for speed
#dateTestBench = [19] 

orderTP = 0
orderSL = 0
orderRank = 0
orderDayfromNow = 0

for testDay in dateTestBench:
	testDate = todayDate + testDay
	daysFromToday = testDate - todayDate 
	testPrediction = np.polyval(model, testDate) 
	desiredRange = Y[0:daysFromToday]
	minRisk = np.std(desiredRange)

	testList = list(range(-100, 101))
	testList = [testPrediction + (std * (x / 100)) for x in testList]
	profits = [x for x in testList if x > currentPrice]
	losses = [x for x in testList if x < currentPrice]

	currentRank = 0
	bestRank = 0
	bestTP = 0
	bestSL = 0

	for i in profits:
		for j in losses:
			reward = i - currentPrice
			risk = currentPrice - j
			rewardrisk = reward / risk
			winrate =  probability(i, testPrediction, std) / (probability(i, testPrediction, std) + probability(j, testPrediction, std))
			currentRank = winrate * reward

			if(currentRank > bestRank):
				if(risk > minRisk/2 and winrate > (1/3) and rewardrisk > 2): 
					if((j > currentPrice - minRisk) and (i < currentPrice + minRisk*2)): 
						bestRank = currentRank
						bestTP = i
						bestSL = j


	if(bestRank > orderRank):
		orderRank = bestRank
		orderTP = bestTP
		orderSL = bestSL
		orderDayfromNow = testDay


#RESULTING OUTPUT
print('Current Price ' + str(currentPrice))
print('Order TP: ' + str(orderTP))
print('Order SL: ' + str(orderSL))
print('Reward-Risk: ' + str((orderTP - currentPrice)/(currentPrice - orderSL)))
print('Win-Rate: ' + str(probability(orderTP, testPrediction, std) / (probability(orderSL, testPrediction, std) + probability(orderTP, testPrediction, std))))
print('Days from Now: ' + str(orderDayfromNow))



#OPTIMIZATION TESTS

#ULTRA SHORT TERM
#1st Degree : 259 in a week, 259 in a month, 263 in 6 months
#2nd Degree : 331 in a week, 333 in a month, 346 in 6 months
#3rd Degree : 339 in a week, 341 in a month, 355 in 6 months
#4th Degree : 336 in a week, 338 in a month, 352 in 6 months
#5th Degree : 314 in a week, 314 in a month, 313 in 6 months

#SHORT TERM
#1st Degree : 267 in 2021, 276 in 2022
#2nd Degree : 361 in 2021, 394 in 2022
#3rd Degree : 373 in 2021, 412 in 2022
#4th Degree : 369 in 2021, 403 in 2022
#5th Degree : 305 in 2021, 269 in 2022

#ULTRA LONG TERM
#1st Degree : 348 in 2030, 438 in 2040
#2nd Degree : 725 in 2030, 1316 in 2040
#3rd Degree : 838 in 2030, 1726 in 2040
#4th Degree : 732 in 2030, 1129 in 2040
#5th Degree : -2710 in 2030, -29026 in 2040

#COMPARISON TO EXTERNAL PREDICTIONS (11/26/25, $486)
#1st Degree: 303
#2nd Degree: 503
#3rd Degree: 545
#4th Degree: 517
#5th Degree: -115

#BEST RESULT : 3rd

#ACCURACY TEST
#Today: 0.34Z
#March Low : -1.41Z
#February High : 0.37Z
#2009 Low : -0.78Z
#2007 High : 0.64Z