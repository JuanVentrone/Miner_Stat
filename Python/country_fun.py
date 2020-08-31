import urllib, json
import requests
import pandas as pd
import math
from bs4 import BeautifulSoup


def blockchain_stats():

    # Español
    # Informacion En estadistica del Blockchain

    # English 
    # Info Blockchain Stats

    url_pool = "https://api.blockchain.info/stats"
    r = requests.get( url_pool )
    datos_varios = r.json()
    
    return datos_varios

def country_price(country):
    

    data = pd.read_csv("country_model_dataset.csv")
    data = data[data["Country"] == country ]
    data = data[['Country','Model','M.B.C USD','Power Consumtion','TH/s','BTC Profit']]
                 
    json = blockchain_stats() 
    market_price=json.get("market_price_usd")

    data["USD Profit"] = data["BTC Profit"].apply(lambda x: (x*market_price) )
    data["Real Profit %"] = ((data["USD Profit"]-data["M.B.C USD"])/data["USD Profit"])*100

    return data