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
from convert import Convert
from date import CgkDate


class CoingeckoCLI:

    def __init__(self):
        self.convert = Convert()
        self.date = CgkDate()
        self.portfolio = Portfolio()

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
        parser_convert.set_defaults(func=self.convert.display_result)
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
        parser_list.set_defaults(func=self.convert.display_list)

        args = parser.parse_args()

        try:
            args.func(args)
        except AttributeError as e:
            msg = f"{e}.\n{Style.BRIGHT}Please run: {Fore.YELLOW}cgk --help{Style.RESET_ALL}"
            self.panic(msg)
        except KeyError as e:
            msg = f"{e}.\n{Style.BRIGHT}Your 'id' or 'vs_currency' was incorrect. Please run: {Fore.YELLOW}cgk L --help{Style.RESET_ALL}"\
            "\nIn case you are sure that you entered them correctly, Coingecko API is overloaded."\
            f"\n{Fore.BLUE}Please try again in a minute.{Style.RESET_ALL}"
            self.panic(msg)



    def panic(self,msg):
        """Error message print"""
        print(f"error: {msg}", file=sys.stderr)
        sys.exit(-1)

if __name__ == '__main__':
    cgk = CoingeckoCLI()
    cgk.parser_main()
