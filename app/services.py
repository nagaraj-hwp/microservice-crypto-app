import requests
import app.validate as validate
from flask import jsonify

def get_market_summaries():
    url = 'https://api.bittrex.com/v3/markets/summaries'
    response = requests.get(url)
    return response.json()

def get_market_summary(symbol):
    if validate(symbol):
        url = f'https://api.bittrex.com/v3/markets/{symbol}/summary'
        response = requests.get(url)
        return response.json()
    return jsonify({'error': 'symbol is empty'})
