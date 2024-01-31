from pycoingecko import CoinGeckoAPI
import argparse  
from datetime import datetime
import requests

class CgkDate:
    """Class to fetch and return date, time for asset price or historical price"""
    
    def __init__(self):
        """Initialize"""  

        #self.time = args.time  
        self.cg = CoinGeckoAPI()

    def historical_date(self):
        """Historical asset price for a given date"""
        id = 'bitcoin'
        date = '28-01-2024'
        # get price for a specific date
        one_date = f"https://api.coingecko.com/api/v3/coins/{id}/history?date={date}&localization=false"
        r = requests.get(one_date)

    def get_unix_time_now(self):
        """Get current date and time"""
        date_time = datetime.now()
        unix_time = date_time.strftime('%Y-%m-%d %H:%M:%S')
        return unix_time
    
  
