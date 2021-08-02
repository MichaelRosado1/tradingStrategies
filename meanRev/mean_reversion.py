'''

The mean_reversion file will contain all of the trading logic required for the mean reversion strategy


'''


class mean_reversion:
    def __init__(self, trader):
        #this will be the trader object that contains all of the buy/sell functions for the api
        self.trader = trader
        self.risk = .001
        
    def calculate_moving_average(self):
        bars = self.trader.get_historical_data()

        total = 0
        for bar in bars:
            total += bar.o
        return total/100

