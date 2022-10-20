# cgk_cmd
Python tools for Coingecko API

## cgk_conv.py
A simple commandline Python tool to get actual market price of any [asset ("id")](https://api.coingecko.com/api/v3/coins/list) against any [vs currency](https://api.coingecko.com/api/v3/simple/supported_vs_currencies). Automatically counts any chosen amount in both directions. 

**Prerequisites**

There 3 Python modules needed. Easy installation with pip.

| Module | Installation |
| --- | --- |
| sys | `pip3 install sys` |
| requests | `pip3 install requests` |
| tabulate | `pip3 install tabulate` |

**Usage**

Run `python3 cgk_conv.py` and follow the given options.
