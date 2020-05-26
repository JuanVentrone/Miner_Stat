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

def block_scrapper_pages(n_pages,n_range_block):

    # Español
    # Escrapea https://www.blockchain.com/btc/blocks Extae valores de cada Bloque

    # Englisg
    # Scrapper https://www.blockchain.com/btc/blocks Get Values from the each Block
    
    
    data_temp=[]
    for i in range(n_pages):
        
        url_pages="https://www.blockchain.com/btc/blocks?page="+str(i+1)

        try:
            url_pages=requests.get(url_pages)
            if url_pages.status_code==200:
                
                # Scrapping the mean Page --- Escrapeo la pagina principal

                sopa=BeautifulSoup(url_pages.text, "html5lib")
                links=sopa.find_all("a",attrs={"class":"sc-1r996ns-0 gzrtQD sc-1tbyx6t-1 kXxRxe iklhnl-0 kVizQZ"})
                links_blocks=[link.get("href") for link in links]
                
                
                # Scrapping each block-page --- Escrapeo cada pagina del bloque

                block_links=[]
                contador=0

                if n_range_block>50:
                    n_range_block-=50
                    c=50
                    print(n_range_block, "entro en mayor a 50")
                else:
                    c=n_range_block
                    print("c es igual a ",c)

                for a in range(c):
                    block_links.append("https://www.blockchain.com"+links_blocks[contador])
                    contador+=3
                    
                for b in block_links:
                    pagina_url= requests.get(b)
                    if pagina_url.status_code==200:
                        
                        lista_h=[]
                        lista_q=[]
                        datos_temporal={}
                        s=BeautifulSoup(pagina_url.text, "html5lib")
                        p = s.find("div",attrs={'class':'sc-1s7qjmx-0 iLEnZs'})

                        h=p.find_all("span",attrs={'class':'sc-1ryi78w-0 gCzMgE sc-16b9dsl-1 kUAhZx sc-1n72lkw-0 lhmHll'})
                        q=p.find_all("span",attrs={'class':'sc-1ryi78w-0 gCzMgE sc-16b9dsl-1 kUAhZx u3ufsr-0 fGQJzg'})
                        
                                   
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
                        
                        data_temp.append(datos_temporal)
                        
                    else:
                        print("No obtuvo Respuesta de :", block_links[contador])
                    
        except Exception as e:
            print("no se encontro la URL:",i+1)
            pass

    return data_temp


def update_blocks_mined():

    # Español:
    # Ejecuta si la tabla esta actualizada o no, para escoger que se debe scrappear

    # English
    # Run if the table is updated or not, to choose what should be scrapped
    
    stats=blockchain_stats()
    n_range_block=stats.get("n_blocks_total")

    if path.exists("Blockchain_Tables/update_mined_blocks.csv"):

        data_old=pd.read_csv("Blockchain_Tables/update_mined_blocks.csv",index_col=0)
        n_range_block=n_range_block-max(data_old["Height"])
        print(n_range_block, max(data_old["Height"]))
        # Verificando si la Tabla esta Actualizada
        
        # Checking if the Table is Updated

        if n_range_block==0:
            print("Los datos estan actualizados al ultimo Bloque Minado ",stats.get("n_blocks_total") )
            return None

        n_pages=math.ceil(n_range_block/50)
        
        # Iniciando el scrapper 
        # Scrapper Innit

        df= block_scrapper_pages(n_pages,n_range_block)

        df_new=pd.DataFrame(df)
        df_new["Height"]=pd.to_numeric(df_new["Height"])
        df_new= df_new.loc[df_new["Height"]>max(data_old["Height"])]
        print(df_new.shape)
        df_suma=pd.concat([df_new,data_old])
        df_suma.drop(df_suma.columns[df_suma.columns.str.contains('unnamed',case = False)],axis = 1, inplace = True)
        df_suma.to_csv("Blockchain_Tables/update_mined_blocks.csv")
        print("El Scrappeo se efectuo con exito")
    else:
        n_pages=math.ceil(n_range_block/50)
        df= block_scrapper_pages(n_pages,n_range_block)
        df_new=pd.DataFrame(df)
        df_new.drop(df_new.columns[df_new.columns.str.contains('unnamed',case = False)],axis = 1, inplace = True)
        df_new.to_csv("Blockchain_Tables/update_mined_blocks.csv")
        

    return print("EL scrappeo se a efectuado exitosamente Primera Actualizacion")


update_blocks_mined()
