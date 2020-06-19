import urllib, json
import requests
import pandas as pd
import math
from bs4 import BeautifulSoup
from Python import procces_table as pt


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

def block_scrapper_pages(n_pages_1,n_range_block):

    # Español
    # Escrapea https://www.blockchain.com/btc/blocks Extae valores de cada Bloque

    # Englisg
    # Scrapper https://www.blockchain.com/btc/blocks Get Values from the each Block


    if type(n_pages_1)==tuple:n_pages_1= range(n_pages_1[0],n_pages_1[-1])
    if type(n_pages_1)==int:n_pages_1= range(0,n_pages_1)
    
    
    data_temp=[]
    data_error=[]
    g=0   
    for i in n_pages_1:
            
        if ((type(n_pages_1)==tuple)+(type(n_pages_1)==range)==1):
            print("Escrapeando pagina: ",i)
            url_pages="https://www.blockchain.com/btc/blocks?page="+str(i)
        else:
            print("escrapeando pagina: ",i+1)
            url_pages="https://www.blockchain.com/btc/blocks?page="+str(i+1)
            

        try:
            url_pages=requests.get(url_pages)
            if url_pages.status_code==200:
                print("BLoques buscados: ",n_range_block)
                # Scrapping the mean Page --- Escrapeo la pagina principal

                sopa=BeautifulSoup(url_pages.text, "html5lib")
                                                       
                links=sopa.find_all("a",attrs={"class":"sc-1r996ns-0 gzrtQD sc-1tbyx6t-1 kXxRxe iklhnl-0 boNhIO"})
                links_blocks=[link.get("href") for link in links]
                
                
           

                # Scrapping each block-page --- Escrapeo cada pagina del bloque

                if type(n_range_block)==range:
                    block_links=finding_blocks(n_range_block,links_blocks,links)
                else:
                    block_links,n_range_block=normal_blocks(n_range_block,links_blocks)
                
                for b in block_links:
                    pagina_url= requests.get(b)
                    if pagina_url.status_code==200:
                        
                        lista_h=[]
                        lista_q=[]
                        datos_temporal={}
                        s=BeautifulSoup(pagina_url.text, "html5lib")
                        p = s.find("div",attrs={'class':'sc-2msc2s-0 glvncZ'})
                    
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
                                                                
                        miner_wallet_link=p.find("a",attrs={'class':'sc-1r996ns-0 gzrtQD sc-1tbyx6t-1 kXxRxe iklhnl-0 boNhIO'})
                        datos_temporal["Miner Name"]=miner_wallet_link.get_text()
                        datos_temporal["URL Miner"]=miner_wallet_link.get("href")
                        
                        g=graph_bar(g)

                        data_temp.append(datos_temporal)
                        
                        
        except Exception as e:
    
            if ((type(n_pages_1)==tuple)+(type(n_pages_1)==range)==1):
                print("no se encontro la URL:",i)
                data_error.append(i)
            else:
                print("no se encontro la URL:",i+1)
                data_error.append(i+1)
            pass
    if data_temp==[]:data_temp=[None]
    return data_temp,data_error

def normal_blocks(n_range_block,links_blocks):
    block_links=[]
    contador=0            
    
    if n_range_block>50:
        n_range_block-=50
        c=50
    else:
        c=n_range_block

    for a in range(c):
        block_links.append("https://www.blockchain.com"+links_blocks[contador])
        contador+=3
    return block_links,n_range_block


def finding_blocks(n_range_block,links_blocks,links):

    block_links=[]
    bloques=[]
    contador=0
    for a in range(50):
        if int(links[contador].get_text()) in n_range_block:
            block_links.append("https://www.blockchain.com"+links_blocks[contador])
        bloques.append(links[contador].get_text())
        contador+=3

    print("Rango de bloques en la pagina: ",min(bloques),"-",max(bloques))

    return block_links

def scrapper_update():
    
    import os.path as path
    
    # Español:
    # Ejecuta si la tabla esta actualizada o no, para escoger que se debe scrappear
    # Esta funcion debe ejecutarse despues de tener una data Hecha solo sirve para actualizar

    # English
    # Run if the table is updated or not, to choose what should be scrapped
    # This function must be executed after having information. It is only used to update
    
    stats=blockchain_stats()
    n_range_block=stats.get("n_blocks_total")

    if path.exists("blockchain data/bc data/old data/data_crudo.csv"):

        data_old=pd.read_csv("blockchain data/bc data/old data/data_crudo.csv")
        data_old.to_csv("blockchain data/bc data/old data/old_data.csv")
        print("diferencias de bloques ",n_range_block, max(data_old["Height"]))
        n_range_block=n_range_block-max(data_old["Height"])
        print(n_range_block)
        # Verificando si la Tabla esta Actualizada
        # Checking if the Table is Updated

        if n_range_block==0:return print("Los datos estan actualizados al ultimo Bloque Minado ",n_range_block)
        
        n_pages=math.ceil(n_range_block/50)
        
        # Iniciando el scrapper 
        # Scrapper Innit

        df,dr= block_scrapper_pages(n_pages,n_range_block)
        if dr==[]:df_suma=table_save_update(df,data_old)
        else:
            df_new=last_scrpapping(df,dr,n_range_block)
            df_suma=table_save_update(df_new,data_old)
        
        df_suma.to_csv("blockchain data/bc data/old data/data_crudo.csv")





    else:
        print("No se puede ejecutar todo el scrappeo, tomaria mucho tiempo puedes ejecutar la Func: scrapper_partitions ",
            " donde puedes particionar el scrapper")

    return print("Funcion scrapper_update COmpleta")

def table_save_update(df_new,data_old):

    df_suma=df_new.append(data_old)
    df_suma=df_suma.sort_values(by=['Height'],ascending=False)
    df_suma=df_suma.drop_duplicates("Height")
    if 'Unnamed: 0' in df_suma:
        df_suma.drop(df_suma.columns[df_suma.columns.str.contains('unnamed',case = False)],axis = 1, inplace = True)
    df_suma=df_suma.dropna()
    return df_suma
    


def scrapper_partitions(page_init,n_times):
    
    # Español:
    # Ejecuta si la tabla esta actualizada o no, para escoger que se debe scrappear
    # page_init: Es el valor donde quieres que empiece el Scrapper
    # n_times: es la posicion final que deseas que termine el Scrappeo
    # Ejemplo: si n_pages_1 empieza en 1000 y n_pages_2 es 200, Scrappea desde el 1000 hasta el 1200

    # English
    # Run if the table is updated or not, to choose what should be scrapper
    # page_init: Is the value pages that you want to start it.
    # n_times: the final position you want the Scrapped, means to end of it
    # Example: if n_pages_1 starts at 1000 and n_pages_2 is 200,maake a Scrappring from 1000 to 1200

        stats=blockchain_stats()
        n_range_block=stats.get("n_blocks_total")
       

        n_pages_1=(page_init,page_init+n_times)
        n_range_block=n_range_block-page_init*50

        df,dr= block_scrapper_pages(n_pages_1,n_range_block)
        df_new=last_scrpapping(df,dr,n_range_block)
        df_new.to_csv("blockchain data/bc data/scrapper partition data/partition_data_"+str(page_init)+"_"+str(page_init+n_times)+".csv")
        
        s=input("¿Desea unir todas las los datos particionados? SI: Presione cualquier tecla")
        if s!="":
            pt.uni_table("blockchain data/bc data/scrapper partition data")
            print("La data sea creado satisfactoriamente blockchain data/bc data/old data/data_crudo.csv")
            return

        return print("EL Scrappeo se efectuo exitosamente: ",page_init,"-",page_init+n_times)

def last_scrpapping(df,dr,n_range_block):

    # Español:
    # Procesado Final para luego guardar el Scrapper

    # English:
    # Final Scrapper Procces

        df_new=pd.DataFrame(df)
        df_2,dr_2= block_scrapper_pages(dr,n_range_block)
        if dr_2!=[]:print("Analizar que ocurre con las paginas:",dr_2)
        if df_2!=[None]:
            df_new_2=pd.DataFrame(df_2)
            df_new=df_new.append(df_new_2)
        # df_new.drop(df_new.columns[df_new.columns.str.contains('unnamed',case = False)],axis = 1, inplace = True)
        return df_new

def scrapper_lost_block():

    # Español:
    # Scrappea los bloques que no fueron scrappeandos anteriormente, Los bloques y el rango de las paginas donde deben estar.
   
    # English
    # Scrap blocks that were not scrapped before, get rank list
       
        data=pd.read_csv("blockchain data/bc data/rang_lost_blocks.csv")
        data.drop(data.columns[data.columns.str.contains('unnamed',case = False)],axis = 1, inplace = True)
        data=data.astype('int64')
        data_temp=pd.DataFrame()

        for i in range(len(data)):
            
            n_pages_1= range(data["Ini Page"][i],data["Final Page"][i])
            n_range_block= range(data["I block"][i],data["F block"][i]+1)
            df,dr= block_scrapper_pages(n_pages_1,n_range_block)
            
            if df!=[None]: 
                if dr!=[]:df=last_scrpapping(df,dr,n_range_block)
                else:df=pd.DataFrame(df)
                data_temp=data_temp.append(df)
            
        
        if "Height" in data_temp:
            
            
            data_temp=data_temp.sort_values(by=['Height'],ascending=False)
            data_temp=data_temp.drop_duplicates("Height")
            if 'Unnamed: 0' in data_temp:data_temp.drop(data_temp.columns[data_temp.columns.str.contains('unnamed',case = False)],axis = 1, inplace = True)
            data_temp=data_temp.dropna
            data_temp.to_csv("blockchain data/bc data/lost range data/new data/find_block"+str(n_range_block)+".csv")
            print("Proceso Exitosamente Finalizado")
            
            

        else:print("No se encontro ninguno de los bloques buscados")
                
    
       
            

def graph_bar(g):
    graph=[" / "," - "," \ "," | "]
    if g==3:
        print("\r",graph[g], end='')
        g=0
    else:
        print("\r",graph[g], end='')
        g+=1
    return g


# Codigo Creado por Juan Vicente Ventrone
# github.com/JuanVentrone
# Creating Code by Juan Vicente Venctrone