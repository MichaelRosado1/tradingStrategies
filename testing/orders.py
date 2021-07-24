import alpaca_trade_api as tradeapi
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

	def check_account_details(self):
		account = self.api.get_account()
		print('${} is available as buying power.'.format(account.buying_power))



def main():
	trader = Trader('AAPL', 10)
	trader.check_account_details()





if __name__ == '__main__':

	main()