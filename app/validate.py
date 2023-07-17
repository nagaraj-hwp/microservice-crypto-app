import re
from flask import jsonify


def validate_symbol(symbol):
    '''
    Validates the symbol parameter for the API endpoint.
    '''
    
    if not symbol:
        raise ValueError("Symbol parameter is required.")
        # return jsonify({'error': 'symbol is empty'})

    if not isinstance(symbol, str):
        raise TypeError("Symbol parameter must be a string.")
        # return jsonify({'error': 'symbol is not a string instance'})

    symbol_regex = r"^([0-9A-Z]{2,5}-[0-9A-Z]{2,4})$"
    if not re.match(symbol_regex, symbol):
        raise ValueError("Invalid symbol format. Symbols can only contain letters, numbers, and hyphens.")
        # return jsonify({'error': 'symbol not matching the regex pattern'})
    
    return True


