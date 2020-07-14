import os
from Python import Scrapper_Blockchain_Func as sf
from Python import procces_table as pt

if __name__=="__main__":
    
    sf.scrapper_update()
    print("1")
    pt.find_lost_block()
    print("2")
    if os.path.exists("blockchain data/bc data/rang_lost_blocks.csv"):
        sf.scrapper_lost_block()
        print("3")
        pt.concat_lost_block()
        os.remove("blockchain data/bc data/rang_lost_blocks.csv")
        print("4")
        pt.find_lost_block()
        print("5")

        if os.path.exists("blockchain data/bc data/rang_lost_blocks.csv"):
            print("ADVERTENCIA: puede haber algun error en la da data_crudo.csv, por favor chequear")
        else:
            pt.coy_file()
    else:
        pt.coy_file()
    if os.path.exists("blockchain data/bc data/rang_lost_blocks.csv"):
        print("ADVERTENCIA: puede haber algun error en la da data_crudo.csv, por favor chequear")
    else:
        pt.coy_file()
        
# ESPAÑOL
# #################################################################################################################
# Este es el codigo con que puedes Scrappear la pagina del www.blockchian.com
# Aunque cada cierto tiempo las clases de los elementos cambian cada cierto tiempo, donde debes inspeccionar los 
# elementos y cambiarloalment manue.
# 
# Scrapper_blockchain_Func es donde esta alojado las funciones para Scrappear
# Procces_table esta alojado donde se trata las particiones escrapeadas, bloques encontrados y se unifican con 
# la data principal que es data_crudo.csv.
# 
# scrapper_update()
# Actualiza la data hasta el ultimo bloque guardado
# 
# scrapper_lost_block()
# Scrappea los bloques faltantes, pero antes debes inspeccionar que bloques faltan
# utilizando la funcion find_lost_block(), si la tabla es muy grande puedes particionarla 
# con: partition_lost_bock()
# 
# 
# scrapper_partitions(page_init,n_times)
# Scrappea los bloques por rango donde page_init es el inicio donde empezara escrapear y n_times y la distancia 
# que scrappea, es decir: page_init=1200  n_times=200, escrappeara de 1200 hasta 1400, cada ciclo son 50 bloques 
# a scrappear 
# 
# 
# procces_table.py 
# concat_partition_data()
# Concatena las particiones ya scrappea con la data principal
# 
# 
# concat_lost_block()
# Concatena las particiones ya scrappeadas de los bloques faltantes con la data principal
# ####################################################################################################################

# INGLES
# #####################################################################################################################
# Which This code you can Scrapper the page of the www.blockchian.com
# Although every so often the classes of the elements change every so often, where you should inspect the
# Element and change it manually.
# 
# 
# Scrapper_blockchain_Func is where the Scrappear functions are hosted
# Procces_table is hosted where cracked partitions, found blocks are treated and unified with
# the main data which is data_crudo.csv.
# 
# scrapper_update()
# Update Data and concact with main Data
# 
# 
# scrapper_lost_block ()
# Scrape the missing blocks, but first you must inspect which blocks are missing
# using the find_lost_block () function, if the table is very big you can partition it
# with: partition_lost_bock ()
# 
# 
# scrapper_partitions (page_init, n_times)
# Scrap the blocks by range where page_init is the start and n_times and the distance between the end.
# Example: page_init = 1200 n_times = 200, that´s mean, from 1200 to 1400, each cycle is 50 blocks
# to scrappear
# 
# 
# procces_table.py
# concat_partition_data ()
# Concatenate the partitions and scrap with the main data
# 
# 
# concat_lost_block ()
# Concatenate the already scrapped partitions of the missing blocks with the main data
# ##############################################################################################################


# Codigo Creado por Juan Vicente Ventrone
# github.com/JuanVentrone
# Creating Code by Juan Vicente Ventrone

