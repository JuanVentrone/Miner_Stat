import pandas as pd
import numpy as np
import math
import Scrapper_Blockchain_Func as sbf
import procces_table as pt

data=pd.read_csv("Blockchain_Tables/rang_paginas_erradas.csv")
data
sbf.scrapper_lost_block()
pt.init_lost_block()
0 in df.columns
data.shape

len(data)/15
data.iloc[[5, 3], data.columns.get_indexer()]
data
171/12
lista=[]



lista=[]
for i in range(15):
    lista.append([i*15,i*15+15])

lista[0]

for i in lista:
    data_temp=data[i[0]:i[1]]
    data_temp.to_csv("blockchain data/bc data/lost range data_"+str(i[0])+"_"+str(i[1])+".csv")
data=pd.read_csv("new_table.csv")
data.shape

if "Height" in data:
    print("esa si era una perra")

pt.find_lost_block()

pt.partition_lost_bock()


data=pd.read_csv("blockchain data/bc data/lost range data/lost_blocks0_14.csv")
data.shape
len(data)
c=0
for i in range(len(data)):
            
    n_pages_1= range(data["Ini Page"][i],data["Final Page"][i])
    n_range_block= range(data["I block"][i],data["F block"][i]+1)
    for i in n_pages_1:
        print("pagina :",i,"bloques:",n_range_block)
        c+=1
print(c)


lista=[]
for i in range(x):
    lista.append([i*x,i*x+x])
lista

len(data)/12

sbf.scrapper_lost_block("blockchain data/bc data/lost range data/lost_blocks0_14.csv")


data_re=pd.read_csv("blockchain data/data_update2020-06-10.csv")
data_re

import numpy as np

x = np.array([[3,6],[5,7]])
y = x.transpose()
a = np.array([1,2])
b = np.array([3,4,5])
print(a+b)
x = 20
not np.any([x%i == 0 for i in range(2, x)])
