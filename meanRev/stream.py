'''
    stream.py will handle all websocket functions and data processing for use in the mean reversion strat
'''
import json
import websocket
import os
from dotenv import load_dotenv

class stream:
    def __init__(self):
        connect()


    def on_open(ws):
        print('opened conection')
        auth_data = {
            'action': 'authenticate',
            'data': {
                    'key_id': os.getenv('API_KEY'),
                    'secret_key': os.getenv('SECRET_KEY')
                }
        }

        ws.send(json.dumps(auth_data))

        listen_message = {'action': 'listen', 'data': {'streams': ['minute.SPY']}}

        ws.send(json.dumps(listen_message))


    def on_message(ws, message):
        #we don't need the entire message, we just need the price data so we can know
        #when to make trades 
        


    def on_close(ws):
        print('closed connection')


    def connect():
        socket = 'wss://data.alpaca.markets/stream'
        
        ws = websocket.WebSocketApp(socket, on_open=on_open, on_message=on_message, on_close=on_close)
        ws.run_forever()

