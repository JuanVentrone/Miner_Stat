import pandas as pd
import numpy as np
import math
from Python import Scrapper_Blockchain_Func as sf
from Python import procces_table as pt


sf.scrapper_update()

pt.concat_lost_block()

pt.find_lost_block()

pt.partition_data_crudo()
pt.partition_lost_bock()

data_1=pd.read_csv("blockchain data/bc data\old data/data_crudo.csv")
data_1.head()
max(data_1["Height"])
min(data_1["Height"])
data_1.shape
