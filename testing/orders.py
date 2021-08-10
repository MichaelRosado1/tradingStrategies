import alpaca_trade_api as tradeapi
import numpy as np
import matplotlib.pyplot as plt
import os
from dotenv import load_dotenv
load_dotenv()


class Trader:
	def __init__(self, symbol='SPY', orderSize=100):
		# self.key_id = os.getenv('API_KEY')
    	# self.secret_key = os.getenv('SECRET_KEY')
        # self.base_url = 'https://paper-api.alpaca.markets'
		self.key_id = os.getenv('API_KEY')
		self.secret_key = os.getenv('SECRET_KEY')
		self.base_url = 'https://paper-api.alpaca.markets'
		self.symbol = symbol
		self.order_size = orderSize
		self.api = tradeapi.REST(
			self.key_id, 
			self.secret_key, 
			self.base_url
		)
	
	def start_trading(self):
		clock = self.api.get_clock()
        #while loop will only start during market hours
		if (clock.is_open):
			self.api.submit_order(
				symbol=self.symbol,
				qty=self.order_size,
				side='buy',
				type='market',
				time_in_force='gtc'
			)
        #I need to do more research on a trading strategy I want to 
        #implement, until then, I will just order single stocks
        #while (clock.is_open):
			#trading logic here
            
            



		

			


		

	def check_account_details(self):
		account = self.api.get_account()
		print('${} is available as buying power.'.format(account.buying_power))
	



def main():
	trader = Trader('AAPL')
	trader.check_account_details()





if __name__ == '__main__':

	main()
