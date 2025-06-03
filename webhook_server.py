from flask import Flask, request, jsonify
import json
from mt5_executor import execute_trade

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    if not data:
        return jsonify({'status': 'error', 'message': 'Invalid JSON'}), 400
    try:
        execute_trade(data)
        return jsonify({'status': 'success', 'message': 'Trade executed'})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
