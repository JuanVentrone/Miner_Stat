import urllib, json
import requests
import pandas as pd
import os.path as path
import math
from bs4 import BeautifulSoup





url_pages="https://www.blockchain.com/btc/blocks?page="+str(1)

        # try:
url_pages=requests.get(url_pages)
if url_pages.status_code==200:
    print("dentro de la condicion 200")
                    # Scrapping the mean Page --- Escrapeo la pagina principal

    sopa=BeautifulSoup(url_pages.text, "html5lib")
    links=sopa.find_all("a",attrs={"class":"sc-1r996ns-0 gzrtQD sc-1tbyx6t-1 kXxRxe iklhnl-0 kVizQZ"})
    links_blocks=[link.get("href") for link in links]
                    
                    
                    # Scrapping each block-page --- Escrapeo cada pagina del bloque

    block_links=[]
    n_bloques_scrapper=[]
    contador=0
    if n_range_block>50:
        n_range_block-=50
        c=50
    else:
        c=n_range_block

    c=int(len(links_blocks)/3)
    for a in range(c):
        block_links.append("https://www.blockchain.com"+links_blocks[contador])
        n_bloques_scrapper.append(links[contador].get_text())
        contador+=3          

n_bloques_scrapper

import Blockchain_Api as ba

stats=ba.blockchain_stats()

stats.get('n_blocks_total')

n_block_last_update=631600
n_range_block= stats.get("n_blocks_total")-n_block_last_update
n_pages=math.ceil(n_range_block/50)
n_pages

if 50<n_range_block:
    n_range_block-=50
else:
    None
import numpy as np
import random as rd
data_ejemplo=[]
data={}
def prueba():
    data["primero"]=rd.random()
    data["segundo"]=rd.random()
    return data
for i in range(4):
    data_ejemplo.append(prueba())
data_ejemplo

# df=pd.DataFrame(data_temp)
# df.to_csv("Blockchain_Tables/History_BLocks_info.csv")

df["Height"]=pd.to_numeric(df["Height"])
df.drop(df[df["Height"]<=max(data_old["Height"])].index, inplace=False)

# def update_block_scrapper():
#     df=pd.DataFrame(block_scrapper_pages())
#     df.to_csv("Blockchain_Tables/History_BLocks_info.csv")
df=block_scrapper_pages()

df.to_csv("tabla_provicional.csv")
df_prueba=df.copy()
# stats=blockchain_stats()
# n_range_block=stats.get("n_blocks_total")
# n_pages=3
# for i in range(n_pages):
#     print(i+1)
df_prueba["Height"]=pd.to_numeric(df_prueba["Height"])
df_prueba.drop(df_prueba[df_prueba["Height"]<=max(data_old["Height"])].index, inplace=False)
min(df_prueba["Height"])

a=9
a-=4
for i in range(1):
    print(i+1)


stats=blockchain_stats()
stats.get("n_blocks_total")
datos=pd.read_csv("tabla_provicional.csv",index_col=0)
datos.drop(datos.columns[datos.columns.str.contains('unnamed',case = False)],axis = 1, inplace = True)
datos
datos.shape
datos_prueba=pd.read_csv("tabla_provicional_prueba.csv")
datos_prueba.shape
datos=datos.drop(["Unnamed: 0","Unnamed: 0.1","Unnamed: 0.1.1","Unnamed: 0.1.1.1","Unnamed: 0.1.1.1.1"],axis=1)
max(datos_prueba["Height"])
datos.to_csv("tabla_provicional.csv")
datos.head()

datos_prueba.shape
datos_prueba["Height"]=pd.to_numeric(datos_prueba["Height"])
datos_prueba=datos_prueba.drop(datos_prueba.iloc[["Height"]<631710].index)
data=data[data["sha"]=="256"]
datos_prueba.head()
max(datos_prueba["Height"])

datos_prueba.to_csv("tabla_provicional_prueba.csv")
datos_prueba=pd.read_csv("tabla_provicional_prueba.csv",index_col=0)


datos_prueba.head()


datos_1= datos_prueba.loc[datos_prueba["Height"]>631710]
datos_2=datos_prueba.loc[datos_prueba["Height"]<631660]
datos_1.to_csv("tabla_provicional_prueba.csv")
df_suma=pd.concat([datos_1,datos_2])
datos_prueba.drop(datos_prueba.columns[datos_prueba.columns.str.contains('unnamed',case = False)],axis = 1, inplace = True)
datos_1.shape
datos_2.shape