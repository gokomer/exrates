# Exrates

Exrates is a simple Python application to get exchange rates from https://exchangeratesapi.io/

## Installation

Exrates requires Python3 and depends on Requests library.

```
pip install exrates
```

## Usage

```
usage: Exrates [-h] [-b BASE] [-c AMOUNT] [-i INTERVAL] [-a ALARM] [--version] symbols

positional arguments:
  symbols               Currencies seperated by comma

options:
  -h, --help            show this help message and exit
  -b BASE, --base BASE  Base currency (default: USD)
  -c AMOUNT, --amount AMOUNT
                        Amount (default: 1)
  -i INTERVAL, --interval INTERVAL
                        Alarm check interval in seconds (default: 1)
  -a ALARM, --alarm ALARM
                        Alarm value to check crossings (default: 0)
  --version             show program's version number and exit
```
## Examples

Base currency is USD

```bash
# exrates try
Base currency is: USD
TRY 6.5815
```

You can set the amount with -c or --amount

```bash
# exrates try 164.5375
Base currency is: USD
TRY 164.5375
```


You can change base currency with -b option

```bash
# exrates try -b eur
Base currency is: EUR
TRY 5.8842199374
```

You can use multiple currencies by seperating them with a comma

```bash
# exrates try,cad
Base currency is: USD
CAD 1.5098
TRY 6.5815
```

You can use set alarm for a certain threshold and get notification

```bash
# exrates try -a 7.50 -i 5
Base currency is: USD
TRY 7.4204
Activated alarms: {'TRY': 7.6574}
```
