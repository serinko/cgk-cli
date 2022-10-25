"""Simple commandline tool to get actual price of any coin on Coingecko and its multiples, modified with argparse"""

#import sys
import requests
from tabulate import tabulate
import numpy as np
import argparse




def get_pycoingecko_ids():
    """Gets a list of all coin ids from coingecko API."""
    url = 'https://api.coingecko.com/api/v3/coins/list'

#    headers = {"id": "accept: application/json"}
    r = requests.get(url)
    # print(f"Status code: {r.status_code}")
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


#def display_help():
#    """Frontend display menu."""
#    msg_0 = "\nCOINGECKO CMD CONVERTOR"
#    line = "========================"
#    msg_1 = "Usage: \npython3 cgk_conv.py <id> <vs_currency> <amount>"\
#            "\n* Example: How much USD is 100 Monero:"\
#            "\n$ python3 cgk_conv.py monero usd 100"
#    msg_2 = "Optional argument <switch>:"\
#            "\n* Switch nominator and denominator."\
#            "\n$ python3 cgk_conv.py <id> <vs_currency> <amount> <switch>"\
#            "\n* Example: How much Monero is 100 USD?, type:"\
#            "\n$ python3 cgk_conv.py monero usd 100 switch"
#    msg_3 = "------------------------\nOptional Commands:"
#    tab = [
#        ["$ python3 cgk_conv.py id_list","Prints all IDs (more than 13000 items!!)"],
#        ["$ python3 cgk_conv.py id_less","Prints a short list of IDs"],
#        ["$ python3 cgk_conv.py vs_list", "Prints a list of vs_currencies (60 items)"],
#        ]
#    print(f"{msg_0}\n{line}\n{msg_1}\n{msg_2}\n{msg_3}")
#    print(tabulate(tab))

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
    
    
#def main_app():
#    """Runs the main program based on passed options"""
#    #print(sys.argv)
#    if len(sys.argv) < 3:
#        if sys.argv[-1] == "id_list":
#            display_id_list()
#        elif sys.argv[-1] == "id_less":
#            display_id_less()
#        elif sys.argv[-1] == "vs_list":
#            display_vs_currencies()
#        else:
#            display_help()
#    else:
#        id = sys.argv[1].lower()
#        vs = sys.argv [2].lower()
#        if len(sys.argv) == 3 or len(sys.argv) == 4 and sys.argv[-1] == "switch":
#            amount = 1
#        else:
#            amount = float(sys.argv[3])
#        if sys.argv[-1].lower() == 'switch':
#            switch = True 
#        else:
#            switch = False
#        x_price = calc_x_price(id,vs,amount,switch)

#        display_result(id,vs,amount,x_price,switch)

def parser_main():
    """Main function initializing ArgumentParser, storing arguments and executing commands."""    
    parser = argparse.ArgumentParser(
            prog='Coingecko Commandline Convertor',
            description='''Convert any asset in any amount in terminal.''',
            epilog='''Let there be dark!'''
        )
    
    parser.add_argument("id", nargs='?', default="store_false",
                    help="add an id of an asset to convert")
    parser.add_argument("vs_currency", nargs='?', 
                    help="add a symbol of a currency to convert to")
    parser.add_argument("amount", type=float, nargs='?',default=1,
                    help="price multiplier, default = 1")

    parser.add_argument("-s", "--switch",
                    action="store_true",
                    help="switches: id <--> vs_currency (xmr to usd <--> usd to xmr)")       
    parser.add_argument("--id_list",
                    help="displays all convertable coin ids (over 13000 items!)", action="store_true")
    parser.add_argument("--id_less",
                    help="displays shortened list of convertable coin ids", action="store_true")
    parser.add_argument("--vs_list",
                    help="displays all vs currencies (~60items)", action="store_true")  
    parser.add_argument("-V","--version", action="version", version='%(prog)s 2.0.1')
    
    
    args = parser.parse_args()

    a = args.id
    b = args.vs_currency
    n = args.amount
    s = args.switch

    if a and b:
        x_price = calc_x_price(a,b,n,s)
        display_result(a,b,n,x_price,s)
    else:
        if args.id_list:
            display_id_list()
        elif args.id_less:
            display_id_less()
        elif args.vs_list:
            display_vs_currencies()
    

if __name__ == '__main__':
#    main_app()
    parser_main()