'''

The mean_reversion file will contain all of the trading logic required for the mean reversion strategy


'''
class mean_reversion:
    def __init__(self, trader):
        #this will be the trader object that contains all of the buy/sell functions for the api
        self.trader = trader
        self.risk = .001
        self.moving_average = None
        self.stop_loss = .002 
        
    def calculate_moving_average(self):
        bars = self.trader.get_historical_data()

        total = 0
        for bar in bars:
            total += bar.o
        ave = total/100

        #We shouldn't calculate this average too often since it is very expensive
        #and will cause too many api calls 
        self.moving_average = ave
        return ave

    def start_trading(self):
        conn = self.trader.__api.stream2.StreamConn(self.trader.__key_id, self.trader.__secret_key, self.trader.__base_url)

        @conn.on(r'^account_updates$')
        async def on_account_updates(conn, channel, account):
            print('account', account)

        @conn.on(r'^trade_updates$')
        async def on_trade_updates(conn, channel, trade):
            print('trade', trade)


