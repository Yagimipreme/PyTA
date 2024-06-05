import sys
import requests
import talib as ta
import numpy as np
from binance import Client
import pandas as pd

def get_data(ticker,interval='1h',start='1 Jan 2023', end=None):
    client = Client()
    intervals = {
        '15min': Client.KLINE_INTERVAL_15MINUTE,
        '1h': Client.KLINE_INTERVAL_1HOUR,
        '4h': Client.KLINE_INTERVAL_4HOUR,
        '1d': Client.KLINE_INTERVAL_1DAY,
    }
    interval = intervals.get(interval,'1h')
    klines = client.get_historical_klines(symbol=ticker, interval=interval, start_str=start,end_str=end)
    data.columns = ['open_time','open', 'high', 'low', 'close', 'volume','close_time', 'qav','num_trades','taker_base_vol','taker_quote_vol', 'ignore']
    data.index = [pd.to_datetime(x, unit='ms').strftime('%Y-%m-%d %H:%M:%S') for x in data.open_time]
    usecols=['open', 'high', 'low', 'close', 'volume', 'qav','num_trades','taker_base_vol','taker_quote_vol']
    data = data[usecols]
    data = data.astype('float')
    return data

get_data("BTC")