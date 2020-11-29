import backtrader as bt
from datetime import datetime
from Downloaddata import getdata

getdata()


cerebro = bt.Cerebro()

cerebro.broker.setcash(56000)
print("Starting Portfolio Value: %.2f" % cerebro.broker.getvalue())

data = bt.feeds.YahooFinanceCSVData(
    dataname='6282.csv',
    fromdate=datetime(2020, 1, 1),
    reverse=False
)

cerebro.adddata(data)
cerebro.run()

print("Final Portfolio Value: %.2f" % cerebro.broker.getvalue())
