#TODO
#- DONE: redo into classes for easier object reference
#- REDUNDANT, implmenet fully: test it as it's own program, copying the logic of convertor
#   - test subcommands for P/portfolio command
#   - init: initialise a new portfolio [--name]
#   - add: add an asset to your portfolio [--name, --id (asset id)] -> asset is listed with 0 values
#   - buy: buy an asset [--name, --id, --amount, --price, --time, --fees, --notes] -> if asset was not added, it adds it
#   - sell: sell an asset [--name, --id, --amount, --price, --time, --fees, --notes] -> if asset was not added, it adds it

#- merge it as a module

#!/usr/bin/python3


"""Portfolio module for cgk cli"""

import requests
from tabulate import tabulate
import numpy as np
import argparse
from tabulate import tabulate
from colorama import Fore, Back, Style
import sys
import os
import toml
from date import CgkDate
import pandas as pd
from convert import Convert

class Portfolio():

    def __init__(self):
        self.date = CgkDate()
        self.convert = Convert()
        self.id_list = self.convert.save_id_list()
        self.data_dir_path = "~/.config/cgk-cli/portfolios/"
        self.create_data_dir = self.convert.create_data_dir()
        self.underlying_asset = self.read_underlying_asset()
        self.config = self.read_config()

    def arg_parser(self,args):
        if args.create:
            self.create_portfolio(args)
        elif args.add_asset:
            self.add_asset(args)
        elif args.buy or args.sell:
            self.buy_sell(args)
        else:
            pass

    def read_config(self):
        home = os.path.expanduser('~')
        file = f"{home}/.config/cgk-cli/config.toml"
        # refresh try-expect-error and implement this instead of this hack
        if os.system(f"test -d {self.data_dir_path}") == 0:
            pass
        else:
            self.create_data_dir()
        if os.system(f"test -f {file}") == 0:
            pass
        else:
            os.system(f"cp data/config.toml {file}")
        with open(file, 'r') as f:
            config = toml.load(f)
        return config

    def read_underlying_asset(self):
       config = self.read_config()
       underlying_asset = config["underlying_asset"]
       return underlying_asset


    def create_portfolio_dir(self,portfolio_name,path):
        dir_exist = f"Portfolio {portfolio_name} already exists, please choose another name!"
        dir_created = f"{Style.BRIGHT}New porfolio {portfolio_name} was initialised.\nData storage is located at {Fore.YELLOW}{path}{Style.RESET_ALL}"
        if os.system(f"test -d {path}") == 0:
            print(dir_exist)
            sys.exit(-1)
        else:
            os.system(f"mkdir -p {path}")
            print(dir_created)

    def create_portfolio(self, args):
        """Creates porftfolio data directory and initial csv file"""
        portfolio_name = args.name
        path = f"{self.data_dir_path}{portfolio_name}"
        if portfolio_name:
            self.create_data_dir()
            self.create_portfolio_dir(portfolio_name,path)
            #df = pd.read_csv("data/portfolio.csv")
            #add a cli function editing new portfolio
            #df.to_csv(f"{path}/{portfolio_name}.csv")
            os.system(f"cp data/portfolio.csv {path}/{portfolio_name}.csv")
        else:
            self.missing_name()

    def create_id_csv(self,args):
        path = f"{self.dir_path}{args.name}/coins"
        file = f"{path}/{id}.csv"
        if os.system(f"test -d {path}") == 0:
            pass
        else:
            os.system(f"mkdir {path}")
        if os.system(f"test -f {file}") == 0:
            pass
        else:
            os.system(f"cp data/asset.csv {file}")
            print("{id}.csv was created, its stored in {path}")


# a few functions here
# add_asset ID - no need for price, just adds to ther list with 0
# buy ID - price total or per coin, time, note (later fees)
# sell ID - price total or per coin, time, note (later fees)

    def get_file(self,name):
        file = f"{self.data_dir_path}{name}/{name}.csv"
        return file

    def buy_sell(self,args):
        if name:
            id = args.id
            file = self.get_file(name)
            while True:
                df = pd.read_scv(file)
                if id in df.Asset.values:
                    path = f"{self.dir_path}{name}/coins/{id}.csv"
                    csv = pd.read_csv(path)
                    transaction, price_per_coin, quantity, total, fees, note = self.buy_sell_cli(args)
                    self.add_transaction(csv, transaction, price_per_coin, quantity, total, fees, note)
                else:
                    prompt = "f{id} is not added in your portfolio.\ndo you want to add it now? y/n"
                    input(prompt)
                    if input == "y" or "Y":
                        self.add_asset(args)
                    else:
                        sys.exit(-1)
        else:
            self.missing_name()

    #def add_transaction(self, csv, transaction, price_per_coin, quantity, total, fees, note):


    def buy_sell_cli(self,args):
        if args.buy:
            transaction = "buy"
        else:
            transaction = "sell"
        while True:
            prompt = f"\nChoose an input you want to add - the rest will be calculated:\
                    \n1. Price per coin & Quantity\
                    \n2. Total {self.underlying_asset} spent/gained & Quantity\
                    \n3. Total {self.underlying_asset} spent/gained & Price per coin\
                    \n(enter 1 or 2 or 3): "
            choose_input = input(prompt)
            if choose_input == "1":
                price_per_coin = input(f"Price per {args.id} in {self.underlying_asset}: ")
                quantity = input(f"Quantity {args.id} you {transaction}: ")
                # Add fees calculation later
                total = self.total_calculation(price_per_coin, quantity)
            elif choose_input == "2":
                total = input(f"Total {self.underlying_asset} spent/gained: ")
                quantity = input(f"Quantity {args.id} you {transaction}: ")
                price_per_coin = self.price_per_coin_calculation(total, quantity)
            elif choose_input == "3":
                total = input(f"Total {self.underlying_asset} spent/gained: ")
                price_per_coin = input(f"Price per {args.id} in {self.underlying_asset}: ")
                quantity = self.calculate_quantity(total, price_per_coin)
            else:
                print(f"Your choice was {choose_input}, that's a non-existing option, try again later")
                sys.exit(-1)
            fees = input(f"Fees in {self.underlying_asset}: ")
            note = input("Notes: ")
            line = "-------------------------"
            table = [
                    ("Transaction type", transaction),
                    (f"Quantity {args.id}", quantity),
                    ("Price per coin", price_per_coin),
                    (f"Total {self.underlying_asset}", total),
                    ("Fees", fees),
                    ("Notes", note)
                    ]
            print(line)
            print("This transaction will be added to your portfolio:")
            print(tabulate(table))
            agree = input("Do you agree? (y/again/exit): ")
            if agree == "y" or "Y":
                return transaction, price_per_coin, quantity, total, fees, note
                break
            elif agree == "again" or "Again" or "AGAIN":
                pass
            elif agree == "exit" or "Exit" or "EXIT":
                sys.exit(-1)
            else:
                print(f"Your choice was {agree}, that's a non-existing option, try again later")
                sys.exit(-1)



    def total_calculation(self, price_per_coin, quantity):
        total = float(price_per_coin) * float(quantity)
        return total

    def price_per_coin_calculation(self, total, quantity):
        price_per_coin = float(total) / float(quantity)
        return price_per_coin

    def calculate_quantity(self, total, price_per_coin):
        quantity = float(total) / float(price_per_coin)
        return quantity

    def add_asset(self,args):
        id = args.add_asset
        name = args.name
        if name:
            file = self.get_file(name)
            df = pd.read_csv(file)
            if self.check_asset_id(id, df) == True:
                df.loc[len(df.index), "Asset"] = id
                df.to_csv(file, inex = False)
                self.create_id_csv(args)
                self.print_asset_added(id,file)
                # show portfolio? y/n --> display portfolio
            else:
                self.incorrect_asset(id)
                # add message: id in df already
        else:
            self.missing_name()
        # add another id? y/n

    def print_asset_added(self,id,file):
        message = \
            f"{id} added to your portfolio {file}"\
            f"Display portfolio with command XXX"
        print(message)
        # Do you want to see portfolio? y/n

    def check_asset_id(self,id, df):
        if id in self.id_list and id not in df.Asset.values:
            return True
        else:
            return False

    def incorret_asset(self,id):
        print(f"Asset {id} is not listed on Coingecko, for more help run :cgk L --id_all")
        sys.exit(-1)

    def missing_name(self):
        print("Missing portfolio --name, please specify with --name <NAME>")
        sys.exit(-1)

    def missing_id(self):
        print("Missing asset ID (for example: cgk P --add_asset bitcoin), for more help run: cgk L --id_all.")
        sys.exit(-1)
