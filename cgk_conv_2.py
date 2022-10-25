"""Simple commandline tool to get actual price of any coin on Coingecko and its multiples, modified with argparse"""

# TODO: 
# DONE: 1) Make optional commands into sub commands https://docs.python.org/3/library/argparse.html#sub-commands
# 2) Add colorama style https://pypi.org/project/colorama/
# 3) Update README for non experienced users.

import requests
from tabulate import tabulate
import numpy as np
import argparse

def get_pycoingecko_ids():
    """Gets a list of all coin ids from coingecko API."""
    url = 'https://api.coingecko.com/api/v3/coins/list'

    r = requests.get(url)
    response_dicts = r.json()
    return response_dicts

def get_pycoingecko_symbols():
    url = 'https://api.coingecko.com/api/v3/simple/supported_vs_currencies'
    r = requests.get(url)
    response_list = r.json()
    return response_list

def get_simple_price(id,vs):
    """Gets a basic pair price from the API."""
    url = \
        f"https://api.coingecko.com/api/v3/simple/price?ids={id}&vs_currencies={vs}"
    r = requests.get(url)
    response_dict = r.json()
    price = response_dict[f"{id}"][f"{vs}"]
    return price

def calc_x_price(id,vs,n,switch):
    """Calculates the price based on pair and amount."""
    price = get_simple_price(id,vs)
    if switch == True:
        x_price=1/price*n
    else:
        x_price = price * n
    return x_price

def display_result(id,vs,amount,x_price,switch):
    """Main Function printing the price of chosen crypto and amount."""
    if switch == True:
        msg = f"\n{amount} {vs}  =  {x_price} {id}\n"
    else:
        msg = f"\n{amount} {id}  = {x_price} {vs}\n"
    print(msg)

def display_id_list():
    """Downloads long list of IDs and prints them as a table."""
    response_dicts = get_pycoingecko_ids()
    lst = []
    for dict in response_dicts:
        lst.append(dict["id"])
    array = get_sorted_array(lst)
    print(tabulate(array))

def display_id_less():
    """A users custom choice of id currencies.""" 
    coins = [
        "bitcoin",
        "ethereum",
        "polkadot",
        "solana",
        "zcash",
        "monero",
        "mobilecoin",
        "avalanche-2",
        "ripple",
        "cardano",
        "terra-luna",
        "matic-network",
        "cosmos",
        "chainlink",
        "bitcoin-cash",
        "bitcoin-cash-sv",
        "ftx-token",
        "algorand",
        "ethereum-classic",
        "stellar",
        "tezos",
        "internet-computer",
        "fantom",
        "dash",
        "uniswap",
        "zencash",
        "komodo",
        "gmx",
        "ethereum-pow-iou",
        "dopex",
        "dopex-rebate-token",
        "looksrare",
        "mina-protocol",
        "thorchain-erc20",
        "thorswap",
        "binancecoin",
        "usd-coin",
        "tether",
        ]
    array = get_sorted_array(coins)
    print(tabulate(array))

def display_vs_currencies():
    """Downloads vs_currencies and prints them as a table."""
    lst = get_pycoingecko_symbols()
    array = get_sorted_array(lst)
    print(tabulate(array))
  
def get_sorted_array(lst,columns=3):
    """Convert a list of strings into a sorted array with desired n of colummns."""
    lst = sorted(lst)
    x = columns - len(lst)%columns
    [lst.append("") for i in range(x) if x < columns]
    rows = int(len(lst)/columns)
    arr = np.array(lst).reshape(rows,columns)
    return arr

def parser_main():
    """Main function initializing ArgumentParser, storing arguments and executing commands."""    
    # Top level parser
    parser = argparse.ArgumentParser(
            prog='Coingecko Commandline Convertor',
            description='''Convert any asset of any amount in terminal.''',
            epilog='''Let there be dark!'''
        )
    parser.add_argument("-v","--version", action="version", version='%(prog)s 2.1.1')
    # List sub-command parser
    subparsers = parser.add_subparsers()
    parser_convert = subparsers.add_parser('convert', help=' -h    shows all the options')
    parser_list = subparsers.add_parser('list', help=' -h   shows all the options')
            
    parser_convert.add_argument("id", nargs='?',
                    help="add an id of an asset to convert")
    parser_convert.add_argument("vs_currency", nargs='?',
                    help="add a symbol of a currency to convert to")
    parser_convert.add_argument("amount", type=float, nargs='?',default=1,
                    help="price multiplier (default = 1)")

    parser_convert.add_argument("-s", "--switch",
                    action="store_true",
                    help="id <--> vs_currency (monero to usd <--> usd to monero)")     
    parser_list = subparsers.add_parser('list')
    parser_list.add_argument("-A","--id_all",
                    help="displays all convertable coin ids (over 13000 items!)", action="store_true")
    parser_list.add_argument("-L","--id_less",
                    help="displays a shortened list of convertable coin ids", action="store_true")
    parser_list.add_argument("-V","--vs_list",
                    help="displays all vs currencies (~60items)", action="store_true")  
    
    args = parser.parse_args()   

    try:
        if args.id and args.vs_currency:
            id = args.id
            vs_currency = args.vs_currency
            n = args.amount
            sw = args.switch
            x_price = calc_x_price(id,vs_currency,n,sw)
            display_result(id,vs_currency,n,x_price,sw)
    except AttributeError: 
        pass          

    try:
        if args.id_all:
            display_id_list()
        elif args.id_less:
            display_id_less()
        elif args.vs_list:
            display_vs_currencies()        
    except AttributeError:
        pass 
    

if __name__ == '__main__':
    parser_main()
