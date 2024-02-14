from pycoingecko import CoinGeckoAPI
import argparse  
from datetime import datetime, date
import requests
import time

class CgkDate:
    """Class to fetch and return date, time for asset price or historical price"""
    
    def __init__(self):
        """Initialize"""   

    def historical_data(self):
        """Historical asset price for a given date"""
        id = 'bitcoin'
        vs = 'usd'
        date = "30-12-2022"
        data = f"https://api.coingecko.com/api/v3/coins/{id}/history?date={date}&localization=False"
        response = requests.get(data)
        response_dict = response.json()
        current_price = response_dict['market_data']['current_price']
        price_usd = current_price['usd']
        print(date)
        print("----------")
        print(id, price_usd)


    def get_unix_time_now(self):
        """Get current date and time"""
        now = datetime.now()
        return now

    def date_to_timestamp(self, date):
        """Define from which date"""
        timestamp = time.mktime(datetime.strptime(date, "%Y/%m/%d").timetuple())
        return timestamp
    
    def time_to(self):
        """Get current unix time"""
        unix_time_to = self.get_unix_time_now()
        return time_to

    def historical_range(self):
        """Historical asset price for date range"""
        asset_data_range = f"https://api.coingecko.com/api/v3/coins/{id}/market_chart/range?vs_currency={vs}&from={self.time_from}&to={self.time_to}&precision=full"
        r = requests.get(asset_data_range)
        return asset_data_range

if __name__ == '__main__':
    cgk = CgkDate()
    cgk.historical_data()

  