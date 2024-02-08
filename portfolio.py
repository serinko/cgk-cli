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
        init = args.init
        portfolio_id = args.id


    def create_data_dir(self,path):
        """Checks and create ~/.config/cgk-cli data storage"""
        exist = "Portfolio with such ID already exists, please choose another name"
        os.system(
                "ls ~/.config/cgk-cli/ || echo 'Creating directory ~/.config/cgk-cli/portfolios . . . ' | mkdir -p ~/.config/cgk-cli/portfolios | echo 'Success!'"
                )
        os.system(
                f"if [[test -d {path} == true ]]; then\
                    echo '{exist}`\
                else\
                    mkdir -p {path} && echo 'Portfolio data storage is located at {path}'\
                fi"
                )


    def create_portfolio(self, args):
        """Creates porftfolio data directory and initial csv file"""
        portfolio_id = args.id
        path = f"~/.config/cgk-cli/portfolios/{portfolio_id}"
        self.create_data_dir(path)
        os.system(f"ls {path} || mkdir -p {path}")
        df = pd.read_csv("data/portfolio.csv")
        df.to_csv(f"{path}/{portfolio_id}.csv")
