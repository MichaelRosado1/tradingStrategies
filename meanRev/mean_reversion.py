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

    def calculate_moving_average(self):
        bars = self.trader.get_historical_data()

        total = 0
        for bar in bars:
            total += bar.o
        ave = total / 100
        self.moving_average = ave
        return ave

    def start_trading(self):
        stream.connect()
