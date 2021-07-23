import alpaca_trade_api as tradeapi
import os
from alpaca_trade_api.entity import Position
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

def main():
	print('hello, world!')




if __name__ == '__main__':
	main()
	t = Trader()