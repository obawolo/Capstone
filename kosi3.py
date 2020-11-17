import pandas as pd
from alpha_vantage.timeseries import TimeSeries
import time
import matplotlib.pyplot as plt
import alpha_vantage as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import SGDRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import classification_report
import numpy as np
api_key = '8FIYTT49ZEZT2GV5'

ts = TimeSeries(key=api_key, output_format='pandas')
data, meta_data = ts.get_intraday(symbol='SPY', interval = '1min', outputsize = 'full')
print (data.keys)
data = data[data != np.nan]

close_data = data['4. close']
percentage_change = close_data.pct_change()
print(percentage_change)

last_change = percentage_change[-1]

if abs(last_change) > 0.0004:
    print("SPY Alert:" + str(last_change))


#sns.pairplot(data, x_vars=['Price'],y_vars='time variables')
#plt.show()
#Creating X and Y
x = data[['1. open', '2. high', '3. low', '5. volume']] 
y = data['4. close']
print(len(y))
#plot data to see if it can be linearly fitted
#plt.scatter(x,y, alpha = 0.7)
#plt.show

x_train, y_train, x_test, y_test = train_test_split(x, y, test_size=0.3,random_state=42)
#take a look at the train dataset
print(x_train)
print(y_train) 
# Create linear regression object
regr = LinearRegression()
regr.fit(x_train, y_train)
predictions = regr.predict(x_test)
print(classification_report(y_test,predictions))
plt.scatter(x_test['1. open'], y_test, 'red')
plt.title('Test Data')
plt.xlabel('time Variables')
plt.ylabel('Price')
plt.plot(regr.predict(x_test), color='red',linewidth=3)
plt.show()
#do standard deviation.
