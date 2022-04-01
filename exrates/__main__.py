#!/usr/bin/env python3
import requests
import argparse
from requests.exceptions import HTTPError
from requests.exceptions import Timeout
import time
import numpy as np


__version__ = "1.0.7"
BASE_URL = "https://api.exchangerate.host/latest"


def getParams():
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter, prog='Exrates')
    parser.add_argument("symbols",
                        type=str,
                        help="Currencies seperated by comma")
    parser.add_argument("-b", "--base",
                        dest='base',
                        type=str,
                        default="USD",
                        help="Base currency")
    parser.add_argument("-c", "--amount",
                        dest='amount',
                        type=str,
                        default="1",
                        help="Amount")
    parser.add_argument("-i", "--interval",
                        dest='interval',
                        type=int,
                        default=1,
                        help="Alarm check interval in seconds")
    parser.add_argument("-a", "--alarm",
                        dest='alarm',
                        type=float,
                        default=0,
                        help="Alarm value to check crossings")
    parser.add_argument('--version', action='version',
                        version=f'{parser.prog} {__version__}')
    results = parser.parse_args()
    params = {'base': f'{results.base.upper()}', 'symbols': f'{results.symbols.upper()}', 'interval': results.interval, 'alarm': results.alarm, 'amount': results.amount}
    return params


def makeRequestForRates(params):
    try:
        response = requests.get(f"{BASE_URL}" + "latest", params=params.items(), timeout=5)
        response.raise_for_status()
    except Timeout:
        print('The request timed out')
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    else:
        return response


def getRates(params):
    response = makeRequestForRates(params)
    try:
        formatted_results = response.json()
    except Exception as e:
        print(f'Cannot parse the response: {e}')
    else:
        return formatted_results


def printRates(params):
    formatted_results = getRates(params)
    print(f"Base currency is: {formatted_results['base']}")
    for k, v in formatted_results['rates'].items():
        print(k, v)


class AlarmWorker:

    def __init__(self, interval, alarm_value, getRates_callback):
        self.interval = interval
        self.alarm_value = alarm_value
        self.getRates_callback = getRates_callback
        self.alarm_state = None

    def run(self):
        while True:
            try:
                response = self.getRates_callback()
            except Exception as e:
                print(f'Cannot fetch rates for alarm: {e}')
                break
            else:
                new_state = self.alarm_state
                if response is not None:
                    new_state = np.array(list(response['rates'].values())) > self.alarm_value

                if self.alarm_state is not None:
                    active_alarm_indices = np.where(new_state != self.alarm_state)[0]
                    if len(active_alarm_indices) > 0:
                        currencies = np.array(list(response['rates'].keys()))
                        rates = np.array(list(response['rates'].values()))
                        active_alarms = dict(zip(currencies[active_alarm_indices], rates[active_alarm_indices]))
                        print(f'Activated alarms: {active_alarms}')
                self.alarm_state = new_state

            time.sleep(self.interval)


def setAlarmForRates(params):
    if params['alarm'] > 0:
        alarm_worker = AlarmWorker(params['interval'], params['alarm'], lambda params=params: getRates(params))
        alarm_worker.run()
        return True
    return False


def main():
    printRates(getParams())
    setAlarmForRates(getParams())


if __name__ == "__main__":
    main()
