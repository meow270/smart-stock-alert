import json, os
from requests import get, Response, exceptions
from pathlib import Path
from database import models
from datetime import *
from dotenv import load_dotenv
load_dotenv()

class Data:
    def __init__(self, time_series, symbol):
        self.time_series = time_series
        self.symbol = symbol
    
    def url_collect(self):
        url = f'https://www.alphavantage.co/query?function=TIME_SERIES_{self.time_series.upper()}&datatype=json&symbol={self.symbol.upper()}&apikey={os.getenv('api_key')}'
        try:
            r = get(url)
            r.raise_for_status()
        except exceptions.HTTPError:
            return None
        r = get(url)
        try:
            r.json()["Meta Data"]
        except KeyError:
            return None
        return r.json()

    
    def save_data(self):
        Sessions = models.Session
        with Sessions as db:
            data_json = self.url_collect()
            for i in data_json["Time Series (Daily)"]:
                data_sql = models.Data_Collect(
                    ticket=self.symbol,
                    date=strptime(i, "%Y-%m-%d").date(),
                    open=data_json["Time Series (Daily)"][i]["1. open"],
                    high=data_json["Time Series (Daily)"][i]["2. high"],
                    low=data_json["Time Series (Daily)"][i]["3. low"],
                    close=data_json["Time Series (Daily)"][i]["4. close"],
                    volume=data_json["Time Series (Daily)"][i]["5. volume"],
                    )
                db.add(data_sql)
            db.commit()
        print('data save')
            
                    
if __name__ == "__main__":
    data = Data('daily', 'aapl')
    data.save_data()