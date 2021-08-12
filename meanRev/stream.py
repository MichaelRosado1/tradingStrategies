'''
    stream.py will handle all websocket functions and data processing for use in the mean reversion strat
'''
import json
import websocket

API_KEY = ''
SECRET_KEY = ''
SYMBOL = ''


def on_open(ws):
    print('opened conection')
    auth_data = {
        'action': 'authenticate',
        'data': {
                'key_id': API_KEY, 
                'secret_key': SECRET_KEY
            }
    }

    ws.send(json.dumps(auth_data))

    #listen_message = {'action': 'listen', 'data': {'streams': ['Q.SPY']}}

    #ws.send(json.dumps(listen_message))


def on_message(ws, message):
    print('recieved message: {}', json.dumps(message, indent=4, sort_keys=True))


def on_close(ws):
    print('closed connection')


def connect():
    socket = 'wss://data.alpaca.markets/stream'
    
    ws = websocket.WebSocketApp(socket, on_open=on_open, on_message=on_message, on_close=on_close)
    ws.run_forever()


# this function is necessary to get the trader info from the algo file
def load_trader(trader):
    API_KEY = trader.key_id
    print(API_KEY)
    SECRET_KEY = trader.secret_key
    SYMBOL = trader.symbol 
