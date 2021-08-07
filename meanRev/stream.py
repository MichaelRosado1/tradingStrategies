'''
    stream.py will handle all websocket functions and data processing for use in the mean reversion strat
'''
import json
import websocket

API_KEY = ''
SECRET_KEY = ''
SYMBOL = ''


def _on_open(ws):
    print('opened conection')

    trader = get_trader()
    auth_data = {
        'action': 'authenticate',
        'data': {'key_id': trader.__key_id, 'secret_key': trader.__secret_key}
    }

    ws.send(json.dumps(auth_data))

    listen_message = {'action': 'listen', 'data': {'streams': ['Q.SPY']}}

    ws.send(json.dumps(listen_message))


def _on_message(ws, message):
    print('recieved message: {}', message)


def on_close(ws):
    print('closed connection')


def connect():
    socket = 'wss://data.alpaca.markets/stream'

    ws = websocket.WebSocketApp(socket, on_open=on_open, on_message=on_message)
    ws.run_forever()


# this function is necessary to get the trader info from the algo file
def load_trader(id, secret_id, symbol):
    API_KEY = id
    SECRET_KEY = secret_id
    SYMBOL = symbol
