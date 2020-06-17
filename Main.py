import pandas as pd
import numpy as np
import math
from Python import Scrapper_Blockchain_Func as sf
from Python import procces_table as pt


sf.scrapper_update()

pt.concat_lost_block()
