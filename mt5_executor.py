
import MetaTrader5 as mt5
import json
from flask import Flask, request

# Initialize MetaTrader 5 connection
mt5.initialize()

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()

    symbol = data.get("symbol")
    action = data.get("action")
    position_type_filter = None

    # Define position type filter based on action
    if "position_type" in data:
        if data["position_type"].lower() == "buy":
            position_type_filter = mt5.POSITION_TYPE_BUY
        elif data["position_type"].lower() == "sell":
            position_type_filter = mt5.POSITION_TYPE_SELL

    # Handle buy and sell orders
    if action == "buy":
        order_type = mt5.ORDER_TYPE_BUY
    elif action == "sell":
        order_type = mt5.ORDER_TYPE_SELL
    elif action == "close":
        # Close position logic
        positions = mt5.positions_get(symbol=symbol)
        if positions:
            for pos in positions:
                if position_type_filter is not None and pos.type != position_type_filter:
                    continue  # Skip other types

                ticket = pos.ticket
                lot = pos.volume
                close_type = mt5.ORDER_TYPE_SELL if pos.type == mt5.POSITION_TYPE_BUY else mt5.ORDER_TYPE_BUY

                close_request = {
                    "action": mt5.TRADE_ACTION_DEAL,
                    "symbol": symbol,
                    "volume": lot,
                    "type": close_type,
                    "position": ticket,
                    "deviation": 10,
                    "magic": 123456,
                    "comment": "Trade closed by webhook",
                    "type_time": mt5.ORDER_TIME_GTC,
                    "type_filling": mt5.ORDER_FILLING_IOC
                }

                result = mt5.order_send(close_request)
                print(f"Close result: {result}")
        else:
            print(f"No open positions to close for {symbol}")
    else:
        print(f"Invalid action received: {action}")

    return "OK", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
