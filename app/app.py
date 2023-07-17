from flask import Flask
import requests
from flask import request, jsonify
import app.validate as validate

app = Flask(__name__)


@app.route('/')
def show_welcome():
    return "Welcome to the web app, navigate to the correct endpoints for your responses 👍"

@app.route('/market-summaries')
def get_market_summaries():
    response = requests.get('https://api.bittrex.com/v3/markets/summaries')
    if response.status_code == 200:
        market_summaries = response.json()
        return jsonify(market_summaries)
    return jsonify({'error': 'Failed to fetch market summaries'})


@app.route('/market-summary')
def get_market_summary():
    symbol = request.args.get('symbol')
    if not validate.validate_symbol(symbol):
        return jsonify({'error': 'Symbol parameter is required'})
    url = f'https://api.bittrex.com/v3/markets/{symbol}/summary'
    response = requests.get(url)
    if response.status_code == 200:
        market_summary = response.json()
        return jsonify(market_summary)
    return jsonify({'error': 'Failed to fetch market summary'})


if __name__ == '__main__':
    app.run()
