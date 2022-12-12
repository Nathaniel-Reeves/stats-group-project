#%%
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
#from statsmodels.stats.proportion import proportion_confint 
#from bioinfokit.analys import stat
#import statsmodels.api as sm
#from statsmodels.formula.api import ols
#import statsmodels.api as sm

print("===================== RAW DATA =====================")
#For 2000 data
data2000 = pd.read_csv("data/FARS2000NationalCSV/ACCIDENT.CSV", encoding_errors='replace')
#For 2020 data
data2020 = pd.read_csv("data/FARS2020NationalCSV/accident.CSV", encoding_errors='replace')

'''!!!!!For use of 2000 data, change "data2020" to "data2000"!!!!!'''
df = pd.DataFrame(data2020)
df2 = pd.DataFrame(data2000)

#utah is state 49
state = 49
oneState = df[df.STATE == state]

#print(oneState)
stateWeather = oneState.WEATHER

print("================== WEATHER DATA =================")

print("Mode:   ", stats.mode(stateWeather, keepdims = False))

clear = 1
rain = 2
sleet = 3
snow = 4
fogSmogSmoke = 5
crosswinds = 6
blowingSand = 7
other = 8
cloudy = 10
blowingSnow = 11
freezingRain = 12
unknown = 99

totalDeathsPerWeather = {
        "Weather": [
            "Clear", 
            "Rain", 
            "Sleet", 
            "Snow", 
            "Fog, Smog, Smoke",
            "CrossWinds", 
            "Other", 
            "Blowing Snow", 
            "Freezing Rain", 
            "Reported as Unknown"
            ], 
            # initialize the counts at zero
            "TotalDeaths": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            }

weatherFatals = data2020[["WEATHER","FATALS"]]
for i in range(len(weatherFatals)):
    if weatherFatals.WEATHER[i] == 1:
        weatherFatals.at[i, "WEATHER"] = "Clear"
        totalDeathsPerWeather["TotalDeaths"][0] += weatherFatals.at[i, "FATALS"]
    elif weatherFatals.WEATHER[i] == 2:
        weatherFatals.at[i, "WEATHER"] = "Rain"
        totalDeathsPerWeather["TotalDeaths"][1] += weatherFatals.at[i, "FATALS"]
    elif weatherFatals.WEATHER[i] == 3:
        weatherFatals.at[i, "WEATHER"] = "Sleet"
        totalDeathsPerWeather["TotalDeaths"][2] += weatherFatals.at[i, "FATALS"]
    elif weatherFatals.WEATHER[i] == 4:
        weatherFatals.at[i, "WEATHER"] = "Snow"
        totalDeathsPerWeather["TotalDeaths"][3] += weatherFatals.at[i, "FATALS"]
    elif weatherFatals.WEATHER[i] == 5:
        weatherFatals.at[i, "WEATHER"] = "Fog, Smog, Smoke"
        totalDeathsPerWeather["TotalDeaths"][4] += weatherFatals.at[i, "FATALS"]
    elif weatherFatals.WEATHER[i] == 6:
        weatherFatals.at[i, "WEATHER"] = "CrossWinds"
        totalDeathsPerWeather["TotalDeaths"][5] += weatherFatals.at[i, "FATALS"]
    elif weatherFatals.WEATHER[i] == 7:
        weatherFatals.at[i, "WEATHER"] = "Other"
        totalDeathsPerWeather["TotalDeaths"][6] += weatherFatals.at[i, "FATALS"]
    elif weatherFatals.WEATHER[i] == 8:
        weatherFatals.at[i, "WEATHER"] = "Blowing Snow"
        totalDeathsPerWeather["TotalDeaths"][7] += weatherFatals.at[i, "FATALS"]
    elif weatherFatals.WEATHER[i] == 9:
        weatherFatals.at[i, "WEATHER"] = "Freezing Rain"
        totalDeathsPerWeather["TotalDeaths"][8] += weatherFatals.at[i, "FATALS"]
    else:
        weatherFatals.at[i, "WEATHER"] = "Reported as Unknown"
        totalDeathsPerWeather["TotalDeaths"][9] += weatherFatals.at[i, "FATALS"]

orgData = pd.DataFrame(totalDeathsPerWeather)
print(orgData)

# create bar plot in normal scale
plt.bar(orgData.Weather, orgData.TotalDeaths)
plt.xticks(rotation=90)
plt.title("Total Fatalities in a Given Weather Condition in 2020")
plt.xlabel("Weather Type")
plt.ylabel("Fatals")
plt.show()

# create bar plot using log scale
fig, ax = plt.subplots()
plt.xticks(rotation=90)
ax.bar(orgData.Weather, orgData.TotalDeaths)
plt.title("Total Fatalities in a Given Weather Conditions in 2020 (Log Scale)")
ax.set_yscale('log')
ax.set_xlabel("Weather Type")
ax.set_ylabel("Fatals")
plt.show()

# Calculate probability statistics based off of total fatalities
totalFatals = sum(orgData.TotalDeaths)
probabilities = {}
other = 0
for row_i in range(len(orgData.Weather)):
    weather = orgData.Weather[row_i]
    deaths = int(orgData.TotalDeaths[row_i])
    prob = deaths/totalFatals
    calc = {"i": weather, "p": prob}
    if prob > 0.05:
        probabilities[weather] = prob
    else:
            other += prob
    probabilities["Other Weather Types"] = other

    result = "Probability of death on %(i)s is %(p)s." % calc
    print(result)

new_lst = [f'{i*100:.1f}%' for i in list(probabilities.values())]

# plot a pie chart on probabilities
plt.pie(list(probabilities.values()), labels=new_lst)
plt.title("Probability of Deaths")
plt.legend(list(probabilities.keys()), loc='upper right')
plt.show()


print("================== LIGHTING DATA =================")

daylight = 1
dark_notLighted = 2
dark_lighted = 3
dawn = 4
dusk = 5
other = 7
notReported = 8
unknown = 9

totalDeathsPerLighting = {
        "Lighting": [
            "Daylight", 
            "Dark - Not Lighted", 
            "Dark - Lighted", 
            "Dawn", 
            "Dusk",
            "Other",  
            "Not Reported", 
            "Reported as Unknown"
            ], 
            # initialize the counts at zero
            "TotalDeaths": [0, 0, 0, 0, 0, 0, 0, 0]
            }

lightFatals = data2020[["LGT_COND","FATALS"]]
for i in range(len(lightFatals)):
    if lightFatals.LGT_COND[i] == 1:
        lightFatals.at[i, "LGT_COND"] = "Daylight"
        totalDeathsPerLighting["TotalDeaths"][0] += lightFatals.at[i, "FATALS"]
    elif lightFatals.LGT_COND[i] == 2:
        lightFatals.at[i, "LGT_COND"] = "Dark - Not Lighted"
        totalDeathsPerLighting["TotalDeaths"][1] += lightFatals.at[i, "FATALS"]
    elif lightFatals.LGT_COND[i] == 3:
        lightFatals.at[i, "LGT_COND"] = "Dark - Lighted"
        totalDeathsPerLighting["TotalDeaths"][2] += lightFatals.at[i, "FATALS"]
    elif lightFatals.LGT_COND[i] == 4:
        lightFatals.at[i, "LGT_COND"] = "Dawn"
        totalDeathsPerLighting["TotalDeaths"][3] += lightFatals.at[i, "FATALS"]
    elif lightFatals.LGT_COND[i] == 5:
        lightFatals.at[i, "LGT_COND"] = "Dusk"
        totalDeathsPerLighting["TotalDeaths"][4] += lightFatals.at[i, "FATALS"]
    elif lightFatals.LGT_COND[i] == 7:
        lightFatals.at[i, "LGT_COND"] = "Other"
        totalDeathsPerLighting["TotalDeaths"][5] += lightFatals.at[i, "FATALS"]
    elif lightFatals.LGT_COND[i] == 8:
        lightFatals.at[i, "LGT_COND"] = "Not Reported"
        totalDeathsPerLighting["TotalDeaths"][6] += lightFatals.at[i, "FATALS"]
    else:
        lightFatals.at[i, "LGT_COND"] = "Reported as Unknown"
        totalDeathsPerLighting["TotalDeaths"][7] += lightFatals.at[i, "FATALS"]

orgData = pd.DataFrame(totalDeathsPerLighting)
print(orgData)

# create bar plot in normal scale
plt.bar(orgData.Lighting, orgData.TotalDeaths)
plt.xticks(rotation=90)
plt.title("Total Fatalities in a Given Lighting Condition in 2020")
plt.xlabel("Lighting Type")
plt.ylabel("Fatals")
plt.show()

# create bar plot using log scale
fig, ax = plt.subplots()
plt.xticks(rotation=90)
ax.bar(orgData.Lighting, orgData.TotalDeaths)
plt.title("Total Fatalities in a Given Lighting Conditions in 2020 (Log Scale)")
ax.set_yscale('log')
ax.set_xlabel("Lighting Type")
ax.set_ylabel("Fatals")
plt.show()

# Calculate probability statistics based off of total fatalities
totalFatals = sum(orgData.TotalDeaths)
probabilities = {}
other = 0
for row_i in range(len(orgData.Lighting)):
    light = orgData.Lighting[row_i]
    deaths = int(orgData.TotalDeaths[row_i])
    prob = deaths/totalFatals
    calc = {"i": light, "p": prob}
    if prob > 0.05:
        probabilities[light] = prob
    else:
            other += prob
    probabilities["Other Lighting Types"] = other

    result = "Probability of death on %(i)s is %(p)s." % calc
    print(result)

new_lst = [f'{i*100:.1f}%' for i in list(probabilities.values())]

# plot a pie chart on probabilities
plt.pie(list(probabilities.values()), labels=new_lst)
plt.title("Probability of Deaths")
plt.legend(list(probabilities.keys()), loc='upper right')
plt.show()

print("===================== Time of Days and CLEAR =====================")

darkNotLighted = oneState[(df.WEATHER == clear)&(df.LGT_COND == dark_notLighted)]
darkLighted = oneState[(df.WEATHER == clear)&(df.LGT_COND == dark_lighted)]
dayLight = oneState[(df.WEATHER == clear)&(df.LGT_COND == daylight)]
dawn = oneState[(df.WEATHER == clear)&(df.LGT_COND == dawn)]
dusk = oneState[(df.WEATHER == clear)&(df.LGT_COND == dusk)]
stateTotal = len(oneState)
darkNL = len(darkNotLighted)
darkL = len(darkLighted)
day = len(dayLight)
dawn = len(dawn)
dusk = len(dusk)

print("Total Utah Accidents:       ", stateTotal)
print("Dark, Not Lighted and Clear:", darkNL, "Chance of Happening:", darkNL/stateTotal)
print("Dark, Lighted and Clear:    ", darkL, "Chance of Happening:", darkL/stateTotal)
print("Daylight and Clear:         ", day, "Chance of Happening:", day/stateTotal)
print("Dawn and Clear:             ", dawn, "Chance of Happening:", dawn/stateTotal)
print("Dusk and Clear:             ", dusk, "Chance of Happening:", dusk/stateTotal, "\n")

print("===================== Time of Days and RAINY =====================")

darkNotLighted = oneState[(df.WEATHER == rain)&(df.LGT_COND == dark_notLighted)]
darkLighted = oneState[(df.WEATHER == rain)&(df.LGT_COND == dark_lighted)]
dayLight = oneState[(df.WEATHER == rain)&(df.LGT_COND == daylight)]
dawn = oneState[(df.WEATHER == rain)&(df.LGT_COND == dawn)]
dusk = oneState[(df.WEATHER == rain)&(df.LGT_COND == dusk)]
darkNL = len(darkNotLighted)
darkL = len(darkLighted)
day = len(dayLight)
dawn = len(dawn)
dusk = len(dusk)

print("Total Utah Accidents:       ", stateTotal)
print("Dark, Not Lighted and Rainy:", darkNL, "Chance of Happening:", darkNL/stateTotal)
print("Dark, Lighted and Rainy:    ", darkL, "Chance of Happening:", darkL/stateTotal)
print("Daylight and Rainy:         ", day, "Chance of Happening:", day/stateTotal)
print("Dawn and Rainy:             ", dawn, "Chance of Happening:", dawn/stateTotal)
print("Dusk and Rainy:             ", dusk, "Chance of Happening:", dusk/stateTotal, "\n")

print("===================== Time of Days and SNOWY =====================")

darkNotLighted = oneState[(df.WEATHER == snow)&(df.LGT_COND == dark_notLighted)]
darkLighted = oneState[(df.WEATHER == snow)&(df.LGT_COND == dark_lighted)]
dayLight = oneState[(df.WEATHER == snow)&(df.LGT_COND == daylight)]
dawn = oneState[(df.WEATHER == snow)&(df.LGT_COND == dawn)]
dusk = oneState[(df.WEATHER == snow)&(df.LGT_COND == dusk)]
darkNL = len(darkNotLighted)
darkL = len(darkLighted)
day = len(dayLight)
dawn = len(dawn)
dusk = len(dusk)

print("Total Utah Accidents:       ", stateTotal)
print("Dark, Not Lighted and Snowy:", darkNL, "Chance of Happening:", darkNL/stateTotal)
print("Dark, Lighted and Snowy:    ", darkL, "Chance of Happening:", darkL/stateTotal)
print("Daylight and Snowy:         ", day, "Chance of Happening:", day/stateTotal)
print("Dawn and Snowy:             ", dawn, "Chance of Happening:", dawn/stateTotal)
print("Dusk and Snowy:             ", dusk, "Chance of Happening:", dusk/stateTotal, "\n")

print("===================== Time of Days and CLOUDY =====================")

darkNotLighted = oneState[(df.WEATHER == cloudy)&(df.LGT_COND == dark_notLighted)]
darkLighted = oneState[(df.WEATHER == cloudy)&(df.LGT_COND == dark_lighted)]
dayLight = oneState[(df.WEATHER == cloudy)&(df.LGT_COND == daylight)]
dawn = oneState[(df.WEATHER == cloudy)&(df.LGT_COND == dawn)]
dusk = oneState[(df.WEATHER == cloudy)&(df.LGT_COND == dusk)]
darkNL = len(darkNotLighted)
darkL = len(darkLighted)
day = len(dayLight)
dawn = len(dawn)
dusk = len(dusk)

print("Total Utah Accidents:       ", stateTotal)
print("Dark, Not Lighted and Cloudy:", darkNL, "Chance of Happening:", darkNL/stateTotal)
print("Dark, Lighted and Cloudy:    ", darkL, "Chance of Happening:", darkL/stateTotal)
print("Daylight and Cloudy:         ", day, "Chance of Happening:", day/stateTotal)
print("Dawn and Cloudy:             ", dawn, "Chance of Happening:", dawn/stateTotal)
print("Dusk and Cloudy:             ", dusk, "Chance of Happening:", dusk/stateTotal, "\n")














# %%
