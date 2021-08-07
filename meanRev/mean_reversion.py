'''

The mean_reversion file will contain all of the trading logic required for the mean reversion strategy


'''
import stream
class mean_reversion:
    def __init__(self, trader):
        self.key_id = trader.__key_id
        self.secret_key = trader.__secret_key
        self.symbol = trader.symbol
        self.risk = .001
        self.moving_average = None
        self.stop_loss = .002
        self.trader = trader

    def calculate_moving_average(self):
        bars = self.trader.get_historical_data()

        total = 0
        for bar in bars:
            total += bar.o
        ave = total/100
        self.moving_average = ave
        return ave

    def start_trading(self):
        stream.load_trader(self.key_id, self.secret_key, self.symbol)
        stream.connect()
