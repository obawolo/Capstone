import backtrader 
import datetime
import matplotlib
from strategy import TestStrategy

cerebro = backtrader.Cerebro()
cerebro.broker.setcash(10000.0)

data = backtrader.feeds.YahooFinanceCSVData(
        dataname= 'oracle.csv',
        # Do not pass values before this date
        fromdate=datetime.datetime(2000, 1, 1),
        # Do not pass values after this date
        todate=datetime.datetime(2010, 12, 31),
        reverse=False)


cerebro.adddata(data)
cerebro.addstrategy(TestStrategy)

cerebro.addsizer(backtrader.sizers.FixedSize, stake=100)


print('Starting Portfolio Value: %.2f' % cerebro.broker.getvalue())

cerebro.run()

print('Final Portfolio Value: %.2f' % cerebro.broker.getvalue())

cerebro.plot() #I used matplotlib  version 3.2.2    C:\Users\Yu Liu\AppData\Local\Programs\Python\Python38>python -m pip install matplotlib==3.2.2