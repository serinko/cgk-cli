import requests
from tabulate import tabulate
import numpy as np
import argparse
from colorama import Fore, Back, Style
import sys
import os
import pandas as pd
from date import CgkDate
from config import Config

class Convert:

    def __init__(self):
        self.date = CgkDate()
        self.data_dir_path = "~/.config/cgk-cli/portfolios/"
        self.config = Config()
        self.api_key = self.get_api_key()
        self.api_demo_string = "x_cg_demo_api_key"
        self.api_pro_string = "x_cg_pro_api_key"

    def get_api_key(self):
        api_key = self.config.get_api_key()
        return api_key

    def create_data_dir(self):
        """Checks and create local data storage"""
        if os.system(f"test -d {self.data_dir_path}") == 0:
            pass
        else:
            print(f"Creating directory {self.data_dir_path} . . . ")
            os.system(f"mkdir -p {self.data_dir_path}")
            print("Success!")


    def get_pycoingecko_ids(self):
        """Gets a list of all coin ids from coingecko API."""
        url = f'https://api.coingecko.com/api/v3/coins/list&{self.api_demo_string}={self.api_key}'
        url2 = 'https://api.coingecko.com/api/v3/coins/list'

        r = requests.get(url2)
        status_code = r.status_code
        if status_code == 200:
            response_dicts = r.json()
            return response_dicts
        else:
            if status_code == 403:
                msg = "Yor IP or API is blocked to query this request, try to change an IP."
            else:
                msg = ""

            self.panic_api_response(status_code, msg)

    def panic_api_response(self, status_code, msg):
            print(f"Error: API response {status_code}\n{msg}", file=sys.stderr)
            sys.exit(-1)

    def get_pycoingecko_symbols(self):
        url = 'https://api.coingecko.com/api/v3/simple/supported_vs_currencies&{self.api_demo_string}={self.api_key}'
        r = requests.get(url)
        response_list = r.json()
        return response_list


    def save_id_list(self):
        """Downloads long list of IDs and prints them as a table."""
        response_dicts = self.get_pycoingecko_ids()
        df = pd.DataFrame(response_dicts)
        ids_list = df['id'].to_list()
        # array = self.get_sorted_array(lst)
        array = pd.Series(ids_list)
        self.create_data_dir()
        array.to_csv("~/.config/cgk-cli/cgk_ids.csv", index=False)
        return ids_list

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
            lenght = len(self.save_id_list())
            os.system("less ~/.config/cgk-cli/cgk_ids.csv")
            print(f"All {lenght} coingecko IDs were saved as ~/.config/cgk-cli/cgk_ids.csv.")
        elif args.id_less:
            self.display_id_less()
        elif args.vs_list:
            self.display_vs_currencies()

    def panic(self,msg):
        """Error message print"""
        print(f"error: {msg}", file=sys.stderr)
        sys.exit(-1)

    def get_simple_price(self,id,vs):
        """Gets a basic pair price from the API."""
        url = \
            f"https://api.coingecko.com/api/v3/simple/price?ids={id}&vs_currencies={vs}&{self.api_demo_string}={self.api_key}"
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
