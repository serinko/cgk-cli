# Python cmd tool for Coingecko API

## ckg.py

A simple command-line app to get actual price of any coin on Coingecko and calculate its multiples, using Coingecko API.

**Version updates** 

- `1.0.0` - crypto converting cmd app works
- `0.1.4` - added aliases (C,L)
- `0.1.3` - made executable
- `0.1.2` - fixed errors
- `0.1.1` - added colorama
- `0.1.0` - sorted into sub-commands
- `0.0.10` - modified with argparse

### Install

Terminal:
```sh
git clone https://github.com/serinko/cgk_cmd
```
Install required modules:

```sh
sudo apt-get install python3
sudo apt-get install python3-pip python-dev
cd cgk_cmd
pip3 install -r requirements.txt
```

In case the requirements installation does not work, install these modules:

| Module | Installation |
| --- | --- |
| requests | `pip3 install requests` |
| tabulate | `pip3 install tabulate` |
| numpy | `pip3 install numpy` |
| argparse | `pip3 install argparse` |
| colorama | `pip3 install colorama` |

Make executable:

```sh
chmod +x cgk.py
```

Create alias - add the alias to your `~/.bashrc` (or `~/.zshrc` in case your native shell is zsh) terminal config:

```sh
alias cgk=~/<path>/cgk_cmd/cgk.py
```

To reload the alias restart your terminal or run:
```sh
source ~/.bashrc
# in case of zsh terminal
source ~/.zshrc
```

### Usage

Print help:

`cgk --help` or `cgk -h`

**Commands**

*Convert [C]*:

help: `cgk C --help`

`cgk C [id] [vs_currency] ([amount] [--switch])`

* `[id]` and `[vs_currency]` are positional (required) arguments
    * To get an asset *id* or *vs_currency* symbols run `cgk L --help` or visit the coingecko documentation page:
        - ["id"](https://api.coingecko.com/api/v3/coins/list)
        - [vs_currency](https://api.coingecko.com/api/v3/simple/supported_vs_currencies)
* `[amount]` is a positional argument - takes arbitrary float value. Default value = 1
* `[--switch]` (or `[-s]`) is an optional argument. Using it switches the direction of the conversion (monero to btc --> btc to monero)

*List [L]*:

Run `cgk L --help` to see how to display all coingecko *id* and *vs_sybols* needed for the *convert | C* subcommand
    
**Examples of cgk usage**

How much Bitcoin is 100 Monero?

`cgk C monero btc 100`

How much Monero is 100 Bitcoin?

`cgk C monero btc 100 --switch` or `cgk C monero btc 100 -s`

How much is ethereum price now? (amount default = 1)
```
cgk C ethereum usd
cgk C ethereum eur
```

How much ethereum is $500?

`cgk ethereum usd 500 --switch`

What `[vs_currency]` symbols can be used in this program?

`cgk L --vs_list` or `cgk L -v`

What `[id]` symbols can be used?

`cgk L --id_all` or `cgk L -a` (Displays over 13000 items!)
`cgk L --id_less` or `cgk L -l` (for a shorter list of *id* items) 


---

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
