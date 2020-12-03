#pip install backtrader
#pip install matplotlib

#Reference: https://backtest-rookies.com/2019/01/04/backtrader-alpha-vantage-data-direct-ingest/

from alpha_vantage.timeseries import TimeSeries
import pandas as pd
import numpy as np
import backtrader as bt
from datetime import datetime

api_key = '8FIYTT49ZEZT2GV5'

#############################################

def alpha_vantage_eod(symbol_list, compact=False, debug=False, *args, **kwargs):
    '''
    Helper function to download Alpha Vantage Data.

    This will return a nested list with each entry containing:
        [0] pandas dataframe
        [1] the name of the feed.
    '''
    data_list = list()

    size = 'compact' if compact else 'full'

    for symbol in symbol_list:

        if debug:
            print('Downloading: {}, Size: {}'.format(symbol, size))

        # Submit our API and create a session
        alpha_ts = TimeSeries(key=api_key, output_format='pandas')

        data, meta_data = alpha_ts.get_daily(symbol=symbol, outputsize=size)

        #Convert the index to datetime.
        data.index = pd.to_datetime(data.index)
        data.columns = ['Open', 'High', 'Low', 'Close','Volume']

        if debug:
            print(data)

        data_list.append((data, symbol))

    return data_list

########################################################

class TestStrategy(bt.Strategy):

    def __init__(self):

        pass

    def next(self):

        for i, d in enumerate(self.datas):

            bar = len(d)
            dt = d.datetime.datetime()
            dn = d._name
            o = d.open[0]
            h = d.high[0]
            l = d.low[0]
            c = d.close[0]
            v = d.volume[0]


            print('{} Bar: {} | {} | O: {} H: {} L: {} C: {} V:{}'.format(dt, bar,dn,o,h,l,c,v))

######################################################

# Create an instance of cerebro
cerebro = bt.Cerebro()

# Add our strategy
cerebro.addstrategy(TestStrategy)

# Setting our initial balance
cerebro.broker.set_cash(1000000)

# Download our data from Alpha Vantage for Cerebro
symbol_list = ['SPY']
data_list = alpha_vantage_eod(
                symbol_list,
                compact=False,
                debug=False)


print(data_list)

for i in range(len(data_list)):

    data = bt.feeds.PandasData(
                dataname=data_list[i][0], # This is the Pandas DataFrame
                name=data_list[i][1], # This is the symbol
                timeframe=bt.TimeFrame.Days,
                compression=1,
                fromdate=datetime(2018,1,1),
                todate=datetime(2019,1,1)
                )

#print(data)



print('Starting Portfolio Value: %.2f' % cerebro.broker.getvalue())

cerebro.run()

print('Final Portfolio Value: %.2f' % cerebro.broker.getvalue())
''