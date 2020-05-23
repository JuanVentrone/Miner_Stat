import urllib, json
import requests
import pandas as pd
import os.path as path
import math
from bs4 import BeautifulSoup

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
    

    return datos_pool,n_bf

def blockchain_stats():

    # Español
    # Informacion En estadistica del Blockchain

    # English 
    # Info Blockchain Stats

    url_pool= "https://api.blockchain.info/stats"
    r = requests.get(url_pool)
    datos_varios=r.json()
    
    return datos_varios


# def block_scrappring_info(links_blocks):

#     # Scrapping each block-page --- Escrapeo cada pagina del bloque aparte
#     block_links=[]
#     contador=0
#     c=int(len(links_blocks)/3)
#     for i in range(c):
#         block_links.append("https://www.blockchain.com"+links_blocks[contador])
#         contador+=3
                    
#     for i in links_blocks:
#         pagina_url= requests.get(block_links[i])
#         if pagina_url.status_code==200:
#             s=BeautifulSoup(pagina_url.text, "html5lib")
#             p = s.find("div",attrs={'class':'sc-1s7qjmx-0 iLEnZs'})

#             h=p.find_all("span",attrs={'class':'sc-1ryi78w-0 gCzMgE sc-16b9dsl-1 kUAhZx sc-1n72lkw-0 lhmHll'})
#             q=p.find_all("span",attrs={'class':'sc-1ryi78w-0 gCzMgE sc-16b9dsl-1 kUAhZx u3ufsr-0 fGQJzg'})
#             lista_h=[]
#             lista_q=[]
                        
#             for i in range(len(q)):
#                 lista_q.append(q[i].get_text())
                        
#             for i in range(len(h)):
#                 lista_h.append(h[i].get_text())
                        
#             lista_h.remove('Miner')
#             lista_q.remove('Learn more about')
#             lista_q.pop(10)
                        
#             for i in range(len(lista_q)):
#                 datos_temporal[lista_h[i]]=lista_q[i]
                        
#             miner_wallet_link=p.find("a",attrs={'class':'sc-1r996ns-0 gzrtQD sc-1tbyx6t-1 kXxRxe iklhnl-0 kVizQZ'})
#             datos_temporal["Miner Name"]=miner_wallet_link.get_text()
#             datos_temporales["URL Miner"]=miner_wallet_link.get("href")
#         else:
#             print("No obtuvo Respuesta de :", block_links[i])
def block_scrapper_pages():

    # Español
    # Escrapea https://www.blockchain.com/btc/blocks Extae valores de cada Bloque

    # Englisg
    # Scrapper https://www.blockchain.com/btc/blocks Get Values from the each Block

    stats=blockchain_stats()
    n_range_block=stats.get("n_blocks_total")
    
    datos_temporal={}


    if path.exists("Blockchain_Tables/History_BLocks_info.csv"):
        data_temp=pd.read_csv("Blockchain_Tables/History_BLocks_info.csv")
        n_range_block=n_range_block-data_temp[0]["Height"]
        
        if n_range_block==0:
            print("Los datos estan actualizados al ultimo Bloque Minado ",stats.get("n_blocks_total") )
            return None
        
    #    n_pages=math.ceil(n_range_block/50)
    n_pages=3

    for i in range(n_pages):
            url_pages="https://www.blockchain.com/btc/blocks?page="+str(i+1)

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
                contador=0
                c=int(len(links_blocks)/3)
                for a in range(c):
                    block_links.append("https://www.blockchain.com"+links_blocks[contador])
                    contador+=3          
                for b in block_links:
                    print(b)
                    pagina_url= requests.get(b)
                    if pagina_url.status_code==200:
                        s=BeautifulSoup(pagina_url.text, "html5lib")
                        p = s.find("div",attrs={'class':'sc-1s7qjmx-0 iLEnZs'})

                        h=p.find_all("span",attrs={'class':'sc-1ryi78w-0 gCzMgE sc-16b9dsl-1 kUAhZx sc-1n72lkw-0 lhmHll'})
                        q=p.find_all("span",attrs={'class':'sc-1ryi78w-0 gCzMgE sc-16b9dsl-1 kUAhZx u3ufsr-0 fGQJzg'})
                        lista_h=[]
                        lista_q=[]
                        print("deep")            
                        for c in range(len(q)):
                            lista_q.append(q[c].get_text())
                                    
                        for d in range(len(h)):
                            lista_h.append(h[d].get_text())
                                    
                        lista_h.remove('Miner')
                        lista_q.remove('Learn more about')
                        lista_q.pop(10)
                                    
                        for e in range(len(lista_q)):
                            datos_temporal[lista_h[e]]=lista_q[e]
                                    
                        miner_wallet_link=p.find("a",attrs={'class':'sc-1r996ns-0 gzrtQD sc-1tbyx6t-1 kXxRxe iklhnl-0 kVizQZ'})
                        datos_temporal["Miner Name"]=miner_wallet_link.get_text()
                        datos_temporal["URL Miner"]=miner_wallet_link.get("href")
                    else:
                        print("No obtuvo Respuesta de :", block_links[i])
                    
        # except Exception as e:
        #     print("no se encontro la URL:",i+1)
        #     pass

    return datos_temporal


data_temp=block_scrapper_pages()

data_temp

# df=pd.DataFrame(data_temp)
# df.to_csv("Blockchain_Tables/History_BLocks_info.csv")


def update_block_scrapper():
    df=pd.DataFrame(block_scrapper_pages())
    df.to_csv("Blockchain_Tables/History_BLocks_info.csv")


stats=blockchain_stats()
n_range_block=stats.get("n_blocks_total")
n_pages=3
for i in range(n_pages):
    print(i+1)