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

    def account_balance(self):
        account = self.api.get_account()
        print('${} is available as on-hand cash.'.format(account.cash))

    def clear_orders(self):
        self.api.cancel_all_orders()

    def submit_order(self):
        self.api.submit_order(
            symbol=self.symbol,
            qty=self.order_size,
            side='buy',
            type='market',
            time_in_force='gtc'
        )

    def sell_order(self):
        self.api.submit_order(
            symbol=self.symbol,
            qty=self.order_size,
            side='sell',
            type='limit',
            time_in_force='gtc'
        )


