"""
Significance of Weather

@author1: Carter Schofield
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats
from scipy import stats
import random
from statsmodels.stats.proportion import proportion_confint 
#from bioinfokit.analys import stat
import statsmodels.api as sm
from statsmodels.formula.api import ols
import statsmodels.api as sm

print("===================== RAW DATA =====================")
#For 2000 data
data2000 = pd.read_csv("data/FARS2000NationalCSV/ACCIDENT.CSV", encoding_errors='replace')
#For 2020 data
data2020 = pd.read_csv("data/FARS2020NationalCSV/accident.CSV", encoding_errors='replace')


'''!!!!!For use of 2000 data, change "data2020" to "data2000"!!!!!'''
df = pd.DataFrame(data2000)

#utah is state 49
print(df.WEATHER)