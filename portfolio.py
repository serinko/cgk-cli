#TODO
#- redo into classes for easier object reference
#- test it as it's own program, copying the logic of convertor
#   - test subcommands for P/portfolio command
#   - init: initialise a new portfolio [--name]
#   - add: add an asset to your portfolio [--name, --id (asset id)] -> asset is listed with 0 values
#   - buy: buy an asset [--name, --id, --amount, --price, --time, --fees, --notes] -> if asset was not added, it adds it
#   - sell: sell an asset [--name, --id, --amount, --price, --time, --fees, --notes] -> if asset was not added, it adds it

#- merge it as a module

#!/usr/bin/python3

class Portfolio:
    def __init__(self):
        self.foo = "bar"

"""Portfolio module for cgk cli"""

import requests
from tabulate import tabulate
import numpy as np
import argparse
from colorama import Fore, Back, Style
import sys
import os
from date import CgkDate
from cgk import CoingeckoCLI
import pandas as pd

class Portfolio():

    def __init__(self):
        self.date = CgkDate()
        self.cgk_cli = CoingeckoCLI()

    def arg_parser(self,args):
        if args.create:
            self.create_portfolio(args)
        elif args.add_asset:
            self.add_asset(args)
        else:
            pass

    def create_data_dir(self):
        """Checks and create local data storage"""
        data_dir_path = "~/.config/cgk-cli/portfolios/"
        if os.system(f"test -d {data_dir_path}") == 0:
            pass
        else:
            print(f"Creating directory {data_dir_path} . . . ")
            os.system(f"mkdir -p {data_dir_path}")
            print("Success!")

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
        path = f"{data_dir_path}{portfolio_name}"
        if portfolio_name:
            self.create_data_dir()
            self.create_portfolio_dir(portfolio_name,path)
            df = pd.read_csv("data/portfolio.csv")
            # add a cli function editing new portfolio
            df.to_csv(f"{path}/{portfolio_name}.csv")
        else:
            self.missing_name()

# a few functions here
# add_asset ID - no need for price, just adds to ther list with 0
# buy ID - price total or per coin, time, note (later fees)
# sell ID - price total or per coin, time, note (later fees)

#    def add_asset(self,args):
#        id = args.add_asset
#        if args.name:
#            self.check_asset_id(id)
#
#        else:
#            self.missing_name()
#
#    def check_asset_id(self,id):
#
#
    def missing_name(self):
        print("Missing portfolio --name, please specify with --name <NAME>")
        sys.exit(-1)

    def missing_id(self):
        print("Missing asset ID (for example: cgk P --add_asset bitcoin), for more help run: cgk L --id_all.")
        sys.exit(-1)
