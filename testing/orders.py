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
		figure = plt.scatter(0, 0)
		#while loop will only start during market hours
		while (clock.is_open):
			#trading logic here
			plt.plot(self.api.get_account().cash)
			plt.show()


		print('market is closed')

		

			


		

	def check_account_details(self):
		account = self.api.get_account()
		print('${} is available as buying power.'.format(account.buying_power))
	



def main():
	trader = Trader('AAPL')
	trader.start_trading()





if __name__ == '__main__':

	main()