#!/usr/bin/env python3
import requests
import argparse
from requests.exceptions import HTTPError
from requests.exceptions import Timeout


__version__ = "1.0"
BASE_URL = "https://api.exchangeratesapi.io/"

def getParams():
    parser = argparse.ArgumentParser(formatter_class = argparse.ArgumentDefaultsHelpFormatter, prog='Exrates')
    parser.add_argument("symbols",
                        type = str,
                        help = "Currencies seperated by comma")
    parser.add_argument("-b", "--base",
                        dest='base',
                        type = str,
                        default = "EUR",
                        help = "Base currency")
    parser.add_argument('--version', action='version',
                        version=f'{parser.prog} {__version__}')
    results = parser.parse_args()
    params = [('base', f'{results.base.upper()}'), ('symbols', f'{results.symbols.upper()}')]
    return params

def getRates(params):
    try:
        response = requests.get(f"{BASE_URL}" + "latest", params=params(), timeout=5)
        response.raise_for_status()
    except Timeout:
        print('The request timed out')
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    else:
        formatted_results = response.json()
        print(f"Base currency is: {formatted_results['base']}")
        for k,v in formatted_results['rates'].items():
            print(k,v)

if __name__ == "__main__":
    getRates(getParams)
