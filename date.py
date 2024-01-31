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

    def stripped_unix_time(self):
        """Stripped time for time_from module"""
        date = self.get_unix_time_now()
        return date

    def hour(self):
        """Extract hour variable"""
        date = self.get_unix_time_now()
        date = str(date)
        time_list = list(date) 
        h = [''.join(time_list[12:14])]
        return h

    def minute(self):
        """Extract minute variable"""
        date = self.get_unix_time_now()
        date = str(date)
        time_list = list(date) 
        m = [''.join(time_list[15:17])]
        return m

    def second(self):
        """Extract second variable"""
        date = self.get_unix_time_now()
        time_list = list(date)
        print(time_list) 
        s = [''.join(time_list[18:21])]
        return s

    def day(self):
        """stripped date for time_from"""
        date = self.get_unix_time_now()
        time_list = list(date)
        d = [''.join(time_list[4:6])]
        return d

    def month(self):
        """stripped date for time_from"""
        date = self.get_unix_time_now()
        time_list = list(date)
        mt = [''.join(time_list[4:6])]
        return mt

    def year(self):
        """stripped date for time_from"""
        date = self.get_unix_time_now()
        time_list = list(date)
        y = [''.join(time_list[:3])]
        return y

    def time_from(self):
        """Define from which date"""
        h = self.hour()
        m = self.minute()
        s = self.second()
        y = self.year()
        date = datetime(y, mt, d, h, m, s)
        timestamp = date.replace.timestamp()
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

  
