import alpaca_trade_api as tradeapi
import os
from dotenv import load_dotenv
load_dotenv()



class MartingaleTrader(object):
    def __init__(self):
        self.key_id = os.getenv('API_KEY')
        self.secret_key = os.getenv('SECRET_KEY')

        self.base_url = 'https://paper-api.alpaca.markets'

        #the ticker that we will be trading
        self.symbol = 'SPY'
        #this will only change if we have an open order or not
        self.current_order = None

        #closing price of last aggregate
        self.last_price = 0

        #api connection
        self.api = tradeapi.REST(
            self.key_id, 
            self.secret_key, 
            self.base_url
        )

        # we need to get the current position
        try:
            #if we are already holding some positions, then set the positions to that quantity
            self.position = int(self.api.get_position(self.symbol).qty)
        except:
            #since we are holding no positions, then set that quantity to 0
            self.position = 0
        
        
    


trade = MartingaleTrader()
print(trade.position)




