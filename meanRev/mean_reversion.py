'''

The mean_reversion file will contain all of the trading logic required for the mean reversion strategy


'''


class mean_reversion:
    def __init__(self, trader):
        #this will be the trader object that contains all of the buy/sell functions for the api
        self.trader = trader
