"""

The mean_reversion file will contain all of the trading logic required for the mean reversion strategy


"""
import stream


class meanReversion:
    def __init__(self, symbol):
        self.symbol = symbol
        self.risk = .001
        self.moving_average = None
        self.stop_loss = .002
        self.last_price = -1 

    def calculate_moving_average(self):
        bars = self.trader.get_historical_data()

        total = 0
        for bar in bars:
            total += bar.o
        ave = total / 100
        self.moving_average = ave
        return ave

    def update_price(self, new_price):
        self.last_price = new_price

    def start_trading(self):
        #websocket connection
        stream.connect()

        if (self.last_price != -1):
            print(last_price)
    



