# cgk_cmd
Python tools for Coingecko API

**Donwloading the repository**

Open terminal in a folder where you want to download it and run:

```bash
$ git clone https://github.com/serinko/cgk_cmd

$ cd cgk_cmd
```

## ckg_conv_2.py
A simple commandline app (v2) to get actual price of any coin on Coingecko and its multiples, using Coingecko API - modified with argparse.

**Install**

Navigate to the directory where you want to have the folder and open terminal.

`git clone https://github.com/serinko/cgk_cmd`

`cd cgk_cmd`

`pip3 install requirements.txt`

**Usage**

* Print help:

`python3 cgk_cmd_2.py --help`

*SubCommands*

* *Convert*:
    - Need to know an asset ["id"](https://api.coingecko.com/api/v3/coins/list) and [vs_currency](https://api.coingecko.com/api/v3/simple/supported_vs_currencies).
    - Run `python3 cgk_cmd_2.py conv <id> <vs_currency> <(--amount)> <(--switch)>`
    - Help `python3 cgk_cmd_2.py conv -h`
    - argument `-s` or `--switch` in the end swaps the direction of conversion (monero to btc --> btc to monero)

* *List*:
    - To display all coin ids or vs_currency symbols, run `python3 cgk_cmd_2.py list -h`
    
Examples:

* How much Bitcoin is 100 Monero?
`python3 cgk_cmd_2.py conv monero btc 100`
* How much Monero is 100 Bitcoin?
'python3 cgk_cmd_2.py conv monero btc 100 -s`


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
