from pycoingecko import CoinGeckoAPI
import argparse  
from datetime import datetime, date
import requests
import time

class CgkDate:
    """Class to fetch and return date, time for asset price or historical price"""
    
    def __init__(self):
        """Initialize"""  

        #self.time = args.time  
        self.cg = CoinGeckoAPI()

    def historical_date(self):
        """Historical asset price for a given date"""
        id = args.id
        date = args.t
        # get price for a specific date
        one_date = f"https://api.coingecko.com/api/v3/coins/{id}/history?date={date}&localization=false"
        r = requests.get(one_date)

    def get_unix_time_now(self):
        """Get current date and time"""
        now = datetime.now()
        return now

    def time_from(self):
        """Define from which date"""
        from_date = args.input_date
        #ts = datetime.timestamp(now)
        timestamp = from_date.replace.timestamp()
        return timestamp
    
    def unix_time_to(self):
        """Get current unix time"""
        unix_time_to = self.get_unix_time_now()
        return time_to

    def historical_range(self):
        """Historical asset price for date range"""
        asset_data_range = f"https://api.coingecko.com/api/v3/coins/{id}/market_chart/range?vs_currency={vs}&from={self.time_from}&to={self.time_to}&precision=full"
        r = requests.get(asset_data_range)
        return asset_data_range
    
if __name__ == '__main__':
    cgkdate = CgkDate()
    cgkdate.time_from()
  
