# Exrates

Exrates is a simple Python application to get exchange rates from https://exchangeratesapi.io/

## Installation

Exrates requires Python3 and depends on Requests library.

```
pip install exrates
```

## Usage

```
usage: Exrates [-h] [-b BASE] [-i INTERVAL] [-a ALARM] [--version] symbols

positional arguments:
  symbols               Currencies seperated by comma

optional arguments:
  -h, --help            show this help message and exit
  -b BASE, --base BASE  Base currency (default: EUR)
  -i INTERVAL, --interval INTERVAL
                        Alarm check interval in seconds (default: 1)
  -a ALARM, --alarm ALARM
                        Alarm value to check crossings (default: 0)
  --version             show program's version number and exit
```
## Examples

Base currency is EUR

```
# exrates try
Base currency is: EUR
TRY 6.5815
```

You can change base currency with -b option

```
# exrates try -b usd
Base currency is: USD
TRY 5.8842199374
```

You can use multiple currencies by seperating them with a comma

```
# exrates try,cad
Base currency is: EUR
CAD 1.5098
TRY 6.5815
```

You can use set alarm for a certain threshold and get notification

```
# exrates try -a 7.50 -i 5
Base currency is: EUR
TRY 7.4204
Activated alarms: {'TRY': 7.6574}
```
