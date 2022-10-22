"""Simple commandline tool to get actual price of any coin on Coingecko and its multiples"""

import sys
import requests
from tabulate import tabulate
import numpy as np

def get_pycoingecko_ids():
    url = 'https://api.coingecko.com/api/v3/coins/list'

    headers = {"id": "accept: application/json"}
    r = requests.get(url, headers)
    # print(f"Status code: {r.status_code}")
    response_dicts = r.json()
    return response_dicts

def get_pycoingecko_symbols():
    url = 'https://api.coingecko.com/api/v3/simple/supported_vs_currencies'
    r = requests.get(url)
    response_list = r.json()
    return response_list

# Commented redundant
#def display_pycoingecko_ids():
#    response_dicts = get_pycoingecko_ids()
#    for dict in response_dicts:
#        for x in dict:
#            print(dict["id"])

#def display_pycoingecko_vs_currencies():
#    response_list = get_pycoingecko_symbols()
#    for x in response_list:
#        print(x)

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


def display_help():
    """Frontend display menu."""
    msg_0 = "\nCOINGECKO CMD CONVERTOR"
    line = "========================"
    msg_1 = "Usage: \npython3 cgk_conv.py <id> <vs_currency> <amount>"\
            "\n* Example: How much USD is 100 Monero:"\
            "\n$ python3 cgk_conv.py monero usd 100"
    msg_2 = "Optional argument <switch>:"\
            "\n* Switch nominator and denominator."\
            "\n$ python3 cgk_conv.py <id> <vs_currency> <amount> <switch>"\
            "\n* Example: How much Monero is 100 USD?, type:"\
            "\n$ python3 cgk_conv.py monero usd 100 switch"
    msg_3 = "------------------------\nOptional Commands:"
    tab = [
        ["$ python3 cgk_conv.py id_list","Prints all IDs (more than 13000 items!!)"],
        ["$ python3 cgk_conv.py id_less","Prints a short list of IDs"],
        ["$ python3 cgk_conv.py vs_list", "Prints a list of vs_currencies (60 items)"],
        ]
    print(f"{msg_0}\n{line}\n{msg_1}\n{msg_2}\n{msg_3}")
    print(tabulate(tab))

def display_id_list():
    """Downloads long list of IDs and prints them as a table."""
    response_dicts = get_pycoingecko_ids()
    list = []
    for dict in response_dicts:
        list.append(dict["id"])
    array = _create_sorted_table(list)
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
    array = _create_sorted_table(coins)
    print(tabulate(array))

def display_vs_currencies():
    """Downloads vs_currencies and prints them as a table."""
    list = get_pycoingecko_symbols()
    array = _create_sorted_table(list)
    print(tabulate(array))

#def _create_sorted_table(lst):
#    array = []
#    new_list = []
#    sorted_list = sorted(lst)
#    n = 0
#    for x in sorted_list:
#        if n%3 == 0:
#            array.append(new_list)
#            new_list = []
#            new_list.append(x)
# 
#        else:
#            new_list.append(x)
#        n += 1
#    array.append(new_list)
#    return array
  
def _create_sorted_table(lst,collumns=3):
    """Convert a list of strings into a sorted array with desired n of colummns."""
    [lst.append("") for x in range(collumns - len(lst)%collumns)]
    rows = int(len(lst)/collumns)
    arr = np.array(sorted(lst)).reshape(rows,collumns)
    return arr
    
    
def main_app():
    """Runs the main program based on passed options"""
    #print(sys.argv)
    if len(sys.argv) < 3:
        if sys.argv[-1] == "id_list":
            display_id_list()
        elif sys.argv[-1] == "id_less":
            display_id_less()
        elif sys.argv[-1] == "vs_list":
            display_vs_currencies()
        else:
            display_help()
    else:
        id = sys.argv[1].lower()
        vs = sys.argv [2].lower()
        if len(sys.argv) == 3 or len(sys.argv) == 4 and sys.argv[-1] == "switch":
            amount = 1
        else:
            amount = float(sys.argv[3])
        if sys.argv[-1].lower() == 'switch':
            switch = True 
        else:
            switch = False
        x_price = calc_x_price(id,vs,amount,switch)

        display_result(id,vs,amount,x_price,switch)

if __name__ == '__main__':
    main_app()
