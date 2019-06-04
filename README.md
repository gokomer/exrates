# Exrates

Exrates is a simple Python application to get exchange rates from https://exchangeratesapi.io/

## Usage

```
usage: Exrates [-h] [-b BASE] [--version] symbols

positional arguments:
  symbols               Currencies seperated by comma

optional arguments:
  -h, --help            show this help message and exit
  -b BASE, --base BASE  Base currency (default: EUR)
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