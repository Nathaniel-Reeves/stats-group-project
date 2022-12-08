
# %%

# pandas = data structure and filtering
import pandas as pd
# numpy = math expressions and converting data types
import numpy as np
# scipy.stats = statistical calculations
from scipy import stats as st
# random = random numbers and random sampling
import random as r
# matplotlib.pyplot = basic plotting
import matplotlib.pyplot as plt
# seaborn = skilled and detailed plotting
import seaborn as sns

import math as m

#          2013-    2018-   2020-
# 2010     2017     2019    Later
# 1         1       1       1       Not an Intersection
# 2         2       2       2       Four-Way Intersection
# 3         3       3       3       T-Intersection
# 4         4       4       4       Y-Intersection
# 5         5       5       5       Traffic Circle
# 6         6       6       6       Roundabout
# 7         7       7       7       Five-Point, or More
# --       10       10      10      L-Intersection
# --       --       --      11      Other Intersection Type
# 8        98       98      98      Not Reported
# 9        99       --      --      Unknown
# --       --       99      99      Reported as Unknown


def getData(filename):
    data = pd.read_csv(filename, encoding_errors="replace")
    return data

def main():
    filepath = "C:/Users/natha/Documents/GitHub/stats-group-project/data/FARS2020NationalCSV/accident.CSV"

    totalDeathsPerIntersection = {"Intersections":["Not an Intersection", "Four-Way Intersection", "T-Intersection", "Y-Intersection", "Traffic Circle", "Roundabout", "Five-Point, or More", "L-Intersection", "Other Intersection", "Reported as Unknown"], "TotalDeaths":[0,0,0,0,0,0,0,0,0,0]}


    accident2020 = getData(filepath)
    intersectionFatals = accident2020[["TYP_INT","FATALS"]]
    for i in range(len(intersectionFatals)):
        if intersectionFatals.TYP_INT[i] == 1:
            intersectionFatals.at[i,"TYP_INT"] = "Not an Intersection"
            totalDeathsPerIntersection["TotalDeaths"][0] += intersectionFatals.at[i,"FATALS"]
        elif intersectionFatals.TYP_INT[i] == 2:
            intersectionFatals.at[i,"TYP_INT"]  = "Four-Way Intersection"
            totalDeathsPerIntersection["TotalDeaths"][1] += intersectionFatals.at[i, "FATALS"]
        elif intersectionFatals.TYP_INT[i] == 3:
            intersectionFatals.at[i,"TYP_INT"]  = "T-Intersection"
            totalDeathsPerIntersection["TotalDeaths"][2] += intersectionFatals.at[i, "FATALS"]
        elif intersectionFatals.TYP_INT[i] == 4:
            intersectionFatals.at[i,"TYP_INT"]  = "Y-Intersection"
            totalDeathsPerIntersection["TotalDeaths"][3] += intersectionFatals.at[i, "FATALS"]
        elif intersectionFatals.TYP_INT[i] == 5:
            intersectionFatals.at[i,"TYP_INT"]  = "Traffic Circle"
            totalDeathsPerIntersection["TotalDeaths"][4] += intersectionFatals.at[i, "FATALS"]
        elif intersectionFatals.TYP_INT[i] == 6:
            intersectionFatals.at[i,"TYP_INT"]  = "Roundabout"
            totalDeathsPerIntersection["TotalDeaths"][5] += intersectionFatals.at[i, "FATALS"]
        elif intersectionFatals.TYP_INT[i] == 7:
            intersectionFatals.at[i,"TYP_INT"]  = "Five-Point, or More"
            totalDeathsPerIntersection["TotalDeaths"][6] += intersectionFatals.at[i, "FATALS"]
        elif intersectionFatals.TYP_INT[i] == 10:
            intersectionFatals.at[i, "TYP_INT"] = "L-Intersection"
            totalDeathsPerIntersection["TotalDeaths"][7] += intersectionFatals.at[i, "FATALS"]
        elif intersectionFatals.TYP_INT[i] == 11:
            intersectionFatals.at[i,"TYP_INT"]  = "Other Intersection"
            totalDeathsPerIntersection["TotalDeaths"][8] += intersectionFatals.at[i, "FATALS"]
        else:
            intersectionFatals.at[i,"TYP_INT"]  = "Reported as Unknown"
            totalDeathsPerIntersection["TotalDeaths"][9] += intersectionFatals.at[i, "FATALS"]

    orgData = pd.DataFrame(totalDeathsPerIntersection)

    print(orgData)

    fig, ax = plt.subplots()
    plt.xticks(rotation=90)
    ax.bar(orgData.Intersections, orgData.TotalDeaths)
    ax.set_yscale('log')
    ax.set_xlabel("Intersection Type")
    ax.set_ylabel("Fatals")
    plt.show()


if __name__ == "__main__":
    main()

# %%
