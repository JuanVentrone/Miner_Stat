import pandas as pd
import numpy as np
import math
from Python import Scrapper_Blockchain_Func as sf




def n_block():
    stats=sf.blockchain_stats()
    return stats.get("n_blocks_total")

def rango_b(a,b,i,block_f,lista_height):

    while a==lista_height[i]:
        if a==b:return print("Finalizo la Busqueda de Bloques no escrapeados")
        a+=1
        i+=1
    block_f.append([a,lista_height[i]])

    a=lista_height[i]
    print(a)
    return rango_b(a,b,i,block_f,lista_height)


def process(block_f):

    page_url_list=[]
    total=n_block()
    for i in block_f:
        
        a=math.ceil(((total-i[0])/50)+2)
        b=math.ceil(((total-i[1])/50)-1)
        page_url_list.append({"Ini Page":b,"Final Page":a,"I block":i[0],"F block":i[1]})

    return page_url_list

def find_lost_block():
    
    data=read_data()
    lista_height=list(data["Height"])
    lista_height.sort()
    a=min(lista_height)
    b=max(lista_height)
    block_f=[]
    i=0 
    rango_b(a,b,i,block_f,lista_height)

    df=process(block_f)
    df_error_pages=pd.DataFrame(df)
    df_error_pages.to_csv("blockchain data/bc data/rang_lost_blocks.csv")
    
    # si deseas activar un escrappeo inmediato
    # r=str(input("El Proceso se realizo exitosamente!,¿Desea Scrappear los Bloques Faltantes,?,Presione cualquier tecla"))
    # if r!="":sf.scrapper_lost_block()

def uni_table(direc):
    g=0
    data=pd.DataFrame()
    import os
    dir_tables=os.listdir(direc)
    
    for i in dir_tables:
        
        try:
            data_temp=pd.read_csv(direc+i)
            data=data.append(data_temp)
            g=sf.graph_bar(g)
        except:
            print("No se pudo concatenar:",direc+i)
            pass
    
    return data
        
def read_data():
    direc="blockchain data/bc data/old data/data_crudo_1.csv"
    print(direc)
    data=pd.read_csv(direc)

    data.drop(data.columns[data.columns.str.contains('unnamed',case = False)],axis = 1, inplace = True)  
    return data

def concat_partition_data():

    # Concatena todos los datos que estan particionados.
    # Para luego unificarlos con la Data principal
    # 
    # Concatenates all the data that are partitioned.
    # Then concattenate with the main data

    data_old=read_data()
    data_new=uni_table("blockchain data/bc data/scrapper partition data")
    data_new=data_old.append(data_new)
    data_new.drop_duplicates("Height", keep='last')
    data_new.to_csv("blockchain data/bc data/partition_data_crudo.csv")
    print("Guardado en blockchain data/bc data/partition_data_crudo.csv")

def concat_lost_block():

    # Concatena todos los datos faltantes ya escrappeados
    # con la data principal
    # 
    # Concatenate all missing and scrapped data with the main data

    data_old=read_data()
    data_new=uni_table("blockchain data/bc data/lost range data/new data/")
    data_new=data_old.append(data_new)
    data_new.drop_duplicates("Height", keep='last')
    data_new.to_csv("blockchain data/bc data/data_crudo_check.csv")
    print("Guardado en blockchain data/bc data/data_crudo_check.csv")

def partition_lost_bock():

    data=pd.read_csv("blockchain data/bc data/rang_lost_blocks.csv")
    x=int(len(data)/12)

    lista=[]
    for i in range(x):
        lista.append([i*x,i*x+x])

    for i in lista:
        data_temp=data[i[0]:i[1]]
        data_temp.to_csv("blockchain data/bc data/lost range data/lost_blocks"+str(i[0])+"_"+str(i[1])+".csv")

def partition_data_crudo():

    data=pd.read_csv("blockchain data/bc data/old data/data_crudo.csv")
    x=int(len(data)/2)
    data_1=data[x:]
    data_2=data[:x]
    data_1.to_csv("blockchain data/bc data/old data/data_crudo_1.csv")
    data_2.to_csv("blockchain data/bc data/old data/data_crudo_2.csv")





# Codigo Creado por Juan Vicente Ventrone
# github.com/JuanVentrone
# Creating Code by Juan Vicente Venctrone