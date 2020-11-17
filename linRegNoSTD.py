import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import sklearn.linear_model
from alpha_vantage.timeseries import TimeSeries
api_key = '8FIYTT49ZEZT2GV5'

ts = TimeSeries(key=api_key, output_format='pandas')
data, meta_data = ts.get_daily_adjusted(symbol='SPY', outputsize = 'full')

data = data.reset_index()
data.plot(x = 'date', y = '4. close')

data['date'] = data['date'].values.astype(float)

X = np.c_[data['date']]
Y = np.c_[data['4. close']]

model = sklearn.linear_model.LinearRegression()
model.fit(X, Y)

date = [[1736208000000000000.0]]
print(model.predict(date))
plt.show()

#standard deviation