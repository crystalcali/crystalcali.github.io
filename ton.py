import requests
import pandas as pd

def get_ton_currency():
    url = 'https://api.coingecko.com/api/v3/coins/markets?vs_currency=rub'
    response = requests.get(url)
    data = response.json()
    df = pd.DataFrame(data)
    TON_CURRENCY = df[df['symbol'] == "ton"]['current_price'].values[0]
    return TON_CURRENCY