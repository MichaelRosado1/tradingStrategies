'''
Trading class to handle:
    buys
    sell
    account information
    day trading limit checks
'''
import alpaca_trade_api as tradeapi
import os
from dotenv import load_dotenv
load_dotenv()

class Trader:
    '''
    @params:
        symbol - the ticker symbol being traded
        order_size - the amount of shares to be traded at a time
    '''
    def __init__(self, symbol='SPY', order_size=10):
        #api keys
        self.key_id = os.getenv('API_KEY')
        self.secret_key = os.getenv('SECRET_KEY')

        #api url
        self.base_url = 'https://paper-api.alpaca.markets'

        #symbol and order information
        self.symbol = symbol
        self.order_size = order_size

        #api connection
        self.api = tradeapi.REST(
            self.key_id,
            self.secret_key,
            self.base_url
        )

    # prints the amount of cash available on the account
    def account_balance(self):
        account = self.api.get_account()
        print('${} is available as on-hand cash.'.format(account.cash))

    #clears all orders
    def clear_orders(self):
        self.api.cancel_all_orders()

    #handles buy orders
    def submit_order(self):
        self.api.submit_order(
            symbol=self.symbol,
            qty=self.order_size,
            side='buy',
            type='market',
            time_in_force='gtc'
        )

    #handles sell orders
    def sell_order(self):
        self.api.submit_order(
            symbol=self.symbol,
            qty=self.order_size,
            side='sell',
            type='limit',
            time_in_force='gtc'
        )

    #prints all the positions in the portfolio
    def view_positions(self):
        portfolio = self.api.list_positions()
        for position in portfolio:
            print('{} shares of {}'.format(position.qty, position.symbol))


    def check_market_open(self):
        clock = self.api.get_clock()
        return clock.is_open

    #function to return a list of bars based on the ticker symbol
    def get_historical_data(self):
        #pulls the data from the last 90 trading days
        barset = self.api.get_barset(self.symbol, 'day', limit=90)
        #this will be only the data from the ticker we chose
        ticker_bar_set = barset[self.symbol]

        #returns an array of bars that contain price information 
        #that we can use to calculate different indicators
        return ticker_bar_set





