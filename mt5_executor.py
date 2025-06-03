import MetaTrader5 as mt5

def execute_trade(data):
    if not mt5.initialize():
        raise Exception("MT5 initialization failed")

    symbol = data.get('symbol')
    lot = data.get('lot', 0.1)
    action = data.get('action')

    if action == 'buy':
        order_type = mt5.ORDER_TYPE_BUY
    elif action == 'sell':
        order_type = mt5.ORDER_TYPE_SELL
    else:
        raise Exception("Invalid action")

    request = {
        "action": mt5.TRADE_ACTION_DEAL,
        "symbol": symbol,
        "volume": lot,
        "type": order_type,
        "price": mt5.symbol_info_tick(symbol).ask if action == 'buy' else mt5.symbol_info_tick(symbol).bid,
        "deviation": 10,
        "magic": 234000,
        "comment": "Trade from webhook",
        "type_time": mt5.ORDER_TIME_GTC,
        "type_filling": mt5.ORDER_FILLING_IOC,
    }

    result = mt5.order_send(request)
    if result.retcode != mt5.TRADE_RETCODE_DONE:
        raise Exception(f"Trade failed: {result.retcode}")

    mt5.shutdown()
