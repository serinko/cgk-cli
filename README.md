# cgk_cmd
Python tools for Coingecko API

## cgk_conv.py
A simple commandline Python tool - Congecko API based convertor to get an actual market price of any [asset ("id")](https://api.coingecko.com/api/v3/coins/list) (13000+) against any [vs currency](https://api.coingecko.com/api/v3/simple/supported_vs_currencies) (60+), in any given amounty in both ways. 

**Prerequisites**

There are few Python modules needed. Easy installation with pip.

| Module | Installation |
| --- | --- |
| sys | `pip3 install sys` |
| requests | `pip3 install requests` |
| tabulate | `pip3 install tabulate` |
| numpy | `pip3 install numpy` |

**Usage**

Run `python3 cgk_conv.py` and follow the given options.

```bash
$ python3 cgk_conv.py        

COINGECKO CMD CONVERTOR
========================
Usage: 
python3 cgk_conv.py <id> <vs_currency> <amount>
* Example: How much USD is 100 Monero:
$ python3 cgk_conv.py monero usd 100
Optional argument <switch>:
* Switch nominator and denominator.
$ python3 cgk_conv.py <id> <vs_currency> <amount> <switch>
* Example: How much Monero is 100 USD?, type:
$ python3 cgk_conv.py monero usd 100 switch
------------------------
Optional Commands:
-----------------------------  -----------------------------------------
$ python3 cgk_conv.py id_list  Prints all IDs (more than 13000 items!!)
$ python3 cgk_conv.py id_less  Prints a short list of IDs
$ python3 cgk_conv.py vs_list  Prints a list of vs_currencies (60 items)
-----------------------------  -----------------------------------------
```
