# TV-to-MT5 Webhook System

This project allows you to receive TradingView alerts via webhook and execute trades on MetaTrader 5 using Python.

## Files
- `webhook_server.py`: Flask server that receives TradingView alerts.
- `mt5_executor.py`: Executes trades on MT5 using MetaTrader5 module.
- `auto_login_mt5.py`: Optional script to auto-login MT5 terminals.
- `requirements.txt`: Python dependencies.
- `Dockerfile`: Docker image for deployment.

## How to Use
1. Install dependencies: `pip install -r requirements.txt`
2. Run `webhook_server.py`
3. Send TradingView alerts in JSON format to `/webhook` endpoint
4. Trades are executed using `mt5_executor.py`
