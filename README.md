# cgk_cmd
Python tools for Coingecko API

## ckg.py
A simple commandline app to get actual price of any coin on Coingecko and its multiples, using Coingecko API.

- *--version: 2.0 - modified with argparse, 2.1 - sorted into subcommands, 2.2 - added colorama, 2.3 - fixed errors, 2.4 - made executable, 2.5 - added aliases (C,L)*

**Install**

Open terminal in desired directory and download the repository:

`git clone https://github.com/serinko/cgk_cmd`

Install required modules:

`cd cgk_cmd`

`pip3 install requirements.txt`

* In case the requirements installation does not work, install these modules:

| Module | Installation |
| --- | --- |
| sys | `pip3 install sys` |
| requests | `pip3 install requests` |
| tabulate | `pip3 install tabulate` |
| numpy | `pip3 install numpy` |
| argparse | `pip3 install argparse` |
| colorama | `pip3 install colorama` |

Make executable:

`chmod +x cgk.py`

**Usage**

* Print help:

`./cgk.py --help`

SubCommands

* *Convert [C]*:
    - Need to know an asset ["id"](https://api.coingecko.com/api/v3/coins/list) and [vs_currency](https://api.coingecko.com/api/v3/simple/supported_vs_currencies). Amount default is set to = 1.
    - Run `./cgk.py C [id] [vs_currency] ([amount] [--switch])`
    - Help `./cgk.py C -h`
    - argument `-s` or `--switch` in the end swaps the direction of conversion (monero to btc --> btc to monero)

* *List [L]*:
    - To display all coin ids or vs_currency symbols, run `./cgk.py L -h`
    
Examples:

* How much Bitcoin is 100 Monero?
`./cgk.py C monero btc 100`
* How much Monero is 100 Bitcoin?
`./cgk.py C monero btc 100 -s`
* What vs_currencies can be used:
`./cgk.py L --vs_list` or shorter `./cgk.py L -v`.


## cgk_conv.py

***An older and simplier version of ckg.py.***

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
