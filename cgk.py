#!/usr/bin/python3

#TODO
#- add error messages
#- add -t/--time [yymmddhhmm, default=now] arg to convert command



import requests
from tabulate import tabulate
import numpy as np
import argparse
from colorama import Fore, Back, Style
import sys
from portfolio import Portfolio
#from date import CgkDate

class CoingeckoConvertor:
    """Simple commandline tool to get a price of any coin on Coingecko and its multiples"""

    def __init__(self):
        self.portfolio = Portfolio()
        #self.date = CgkDate()

    def get_pycoingecko_ids(self):
        """Gets a list of all coin ids from coingecko API."""
        url = 'https://api.coingecko.com/api/v3/coins/list'

        r = requests.get(url)
        response_dicts = r.json()
        return response_dicts

    def get_pycoingecko_symbols(self):
        url = 'https://api.coingecko.com/api/v3/simple/supported_vs_currencies'
        r = requests.get(url)
        response_list = r.json()
        return response_list

    def display_id_list(self):
        """Downloads long list of IDs and prints them as a table."""
        response_dicts = self.get_pycoingecko_ids()
        lst = []
        for dict in response_dicts:
            lst.append(dict["id"])
        array = self.get_sorted_array(lst)
        print(tabulate(array))

    def display_id_less(self):
        """A users custom choice of id currencies."""
        coins = [
            "bitcoin",
            "ethereum",
            "monero",
            "nym",
            "polkadot",
            "solana",
            "zcash",
            "mobilecoin",
            "avalanche-2",
            "ripple",
            "cardano",
            "matic-network",
            "cosmos",
            "chainlink",
            "bitcoin-cash",
            "algorand",
            "ethereum-classic",
            "stellar",
            "tezos",
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
        array = self.get_sorted_array(coins)
        print(tabulate(array))

    def display_vs_currencies(self):
        """Downloads vs_currencies and prints them as a table."""
        lst = self.get_pycoingecko_symbols()
        array = self.get_sorted_array(lst)
        print(tabulate(array))

    def get_sorted_array(self,lst,columns=3):
        """Convert a list of strings into a sorted array with desired n of colummns."""
        lst = sorted(lst)
        x = columns - len(lst)%columns
        [lst.append("") for i in range(x) if x < columns]
        rows = int(len(lst)/columns)
        arr = np.array(lst).reshape(rows,columns)
        return arr

    def display_list(self, args):
        """Function called L subcommand in parser_main"""
        if args.id_all:
            display_id_list()
        elif args.id_less:
            display_id_less()
        elif args.vs_list:
            self.display_vs_currencies()

    def panic(self,msg):
        """Error message print"""
        print(f"error: {msg}", file=sys.stderr)
        sys.exit(-1)

    def get_simple_price(self,id,vs):
        """Gets a basic pair price from the API."""
        url = \
            f"https://api.coingecko.com/api/v3/simple/price?ids={id}&vs_currencies={vs}"
        r = requests.get(url)
        response_dict = r.json()
        price = response_dict[f"{id}"][f"{vs}"]
        return price

    def calc_x_price(self,id,vs,n,switch):
        """Calculates the price based on pair and amount."""
        price = self.get_simple_price(id,vs)
        if switch == True:
            x_price=1/price*n
        else:
            x_price = price * n
        return x_price

    def display_result(self,args):
        """Main Function printing the price of chosen crypto and amount."""
        id = args.id
        vs = args.vs_currency
        amount = args.amount
        switch = args.switch
        #date = args.date

        #if date == True:
         #   display_asset_price_history(self,args)
        #else:    
        x_price = self.calc_x_price(id,vs,amount,switch)
        if switch == True:
            msg = f"\n{amount} {vs}  =  {x_price} {id}\n"
        else:
            msg = f"\n{amount} {id}  =  {x_price} {vs}\n"
        print(Fore.CYAN + Style.BRIGHT + msg)

    #def display_asset_price_history(self,args):
        #"""Display given asset price history within range"""
        #id = args.id
        #date = args.date

        #print(f"\n{date} {id}/{vs} {price})
    
            


    def parser_main(self):
        """Main function initializing ArgumentParser, storing arguments and executing commands."""
        # Top level parser
        parser = argparse.ArgumentParser(
                prog= Style.BRIGHT + 'Coingecko Commandline Convertor' + Style.RESET_ALL,
                description='''Convert any asset of any amount in terminal.''',
                epilog=Style.DIM + '''Let there be dark!''' + Style.RESET_ALL
            )
        parser.add_argument("-V","--version", action="version", version='%(prog)s 1.0.0')
        # Sub-command parsers
        subparsers = parser.add_subparsers(help="{subcommand}[-h] shows all the options")
        parser_convert = subparsers.add_parser('convert',help='{C}[id][vs_currency]([--amount][--switch]) - example: ./cgk.py C monero btc 10', aliases=['C'])
        parser_list = subparsers.add_parser('list', help='displays list of convertable coins {L}[--argument]',aliases=['L'])
        # Convert - arguments
        parser_convert.add_argument("id",
                        help="add an id of an asset to convert")
        parser_convert.add_argument("vs_currency",
                        help="add a symbol of a currency to convert to")
        parser_convert.add_argument("amount", type=float, nargs='?', default=1,
                        help="price multiplier (default = 1)")
        parser_convert.add_argument("-s", "--switch",
                        action="store_true",
                        help="id <--> vs_currency (monero to usd --> usd to monero)")
        parser_convert.set_defaults(func=self.display_result)
        #parser_convert.add_argument("-d", "--date",
         #               action="start date for asset price",
          #              help="format is yyyy/m/dd")
        #parser_convert.set_defaults(func=self.display_result)
        # List - arguments
        parser_list.add_argument("-a","--id_all",
                        help="displays all convertable coin ids (over 13000 items!)", action="store_true")
        parser_list.add_argument("-l","--id_less",
                        help="displays a shortened list of convertable coin ids", action="store_true")
        parser_list.add_argument("-v","--vs_list",
                        help="displays all vs currencies (~60items)", action="store_true")
        parser_list.set_defaults(func=self.display_list)

        args = parser.parse_args()

        try:
            args.func(args)
        except AttributeError as e:
            msg = f"{e}.\n{Style.BRIGHT}Please run: {Fore.YELLOW}cgk --help{Style.RESET_ALL}"
            self.panic(msg)


if __name__ == '__main__':
    cgk = CoingeckoConvertor()
    cgk.parser_main()
