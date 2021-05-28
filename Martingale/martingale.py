import alpaca_trade_api as tradeapi
import os
from alpaca_trade_api.entity import Position
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
        

    def send_order(self, target_qty):
        if self.current_order is not None:
            self.api.cancel_order(self.current_order.id)
        
        #diff between the amount we want to buy and the amount that we are currently holding
        delta = target_qty - self.position

        if delta == 0:
            #we don't want to do anything in this case
            return
        
        print(f'Ordering towards {target_qty}...')

        try:
            if delta > 0:
                #the amount we want to buy is delta
                buy_qty = delta

                if self.position < 0:
                    buy_qty = min(abs(self.position), buy_qty)
                print(f'Buying {buy_qty} shares.')

                self.current_order = self.api.submit_order(
                    self.symbol, buy_qty, 'buy', 'limit', 'day', self.last_price
                )
            #if delta is less than 0, we are going to want to sell shares not buy
            elif delta < 0:
                sell_qty = abs(delta)
                if self.position > 0:
                    sell_qty = min(abs(self.position), sell_qty)
                print(f'Selling {sell_qty} shares')
                self.current_order = self.api.submit_order(
                    self.symbol, sell_qty, 'sell', 'limit', 'day', self.last_price
                )
        
        except Exception as e:
            print(e)
                
    @conn.on(r'trade_updates')
    async def handle_trade(self, conn, channel, data):
        symbol = data.order['symbol']
        if symbol != self.symbol:
            #this means that this is not an order that we are looking to work with
            return
        
        event_type = data.event
        qty = data.order['filled_qty']
        side = data.order['side']
        oid = data.order['id']

        if event_type == 'fill' or event_type == 'partial_fill':
            self.position = int(data.position_qty)
            print(f'New position size due to order fill: {self.position}')
            if (event_type == 'fill' and self.current_order and self.current_order.id == oid):
                self.current_order = None

        elif event_type == 'rejected' or event_type == 'canceled':
            if self.current_order and self.current_order and self.current_order.id == oid:
                self.current_order = None

        elif event_type != 'new':
            print(f'Unexpected order event type {event_type} received')

    conn.run(['trade_updates'])


    @conn.on(r'A$', [self.symbol])
    async def handle_agg(self, conn, channel, data):
        tick_open = self.last_price
        tick_close = data.close
        self.last_price = tick_close
    
    conn.run([f'A.{self.symbol}'])

        
if __name__ == '__main__':
    trader = MartingaleTrader()

    trader.send_order(5)
        
    






