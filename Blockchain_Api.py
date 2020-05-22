import urllib, json
import requests
import pandas as pd

def pool_pie():
    # Español
    # Una estimación de la distribución de hashrate entre los mayores grupos mineros.
    # Basado en un porcentaje de los Bloques Minado por cada Pool

    # English
    # An estimation of hashrate distribution amongst the largest mining pools.
    # Based on a percentage of the blocks mined for each Pool

    url_pool= "https://api.blockchain.info/pools?timespan=7days"
    r = requests.get(url_pool)
    datos_json=r.json()
    datos_json
    
    datos_pool=pd.DataFrame(datos_json.items(), columns=['Pool', 'Block_Founds'])
    n_bf=sum(datos_pool["Block_Founds"])

    datos_pool["BF_Percent"]=datos_pool["Block_Founds"]/n_bf
    pd.options.display.float_format = '{:,.4f}'.format

    return datos_pool,n_bf

def blockchain_stats():

    # Español
    # Informacion En estadistica del Blockchain

    # English 
    # Info Blockchain Stats

    url_pool= " https://api.blockchain.info/stats"
    r = requests.get(url_pool)
    datos_varios=r.json()
    
    return datos_varios


