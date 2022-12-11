
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

import os

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
    # get data from file
    filepath = "../data/FARS2020NationalCSV/accident.csv"
    accident2020 = getData(filepath)

    # create a frame to total death counts from each intersection
    totalDeathsPerIntersection = {
        "Intersections": [
            "Not an Intersection", 
            "Four-Way Intersection", 
            "T-Intersection", 
            "Y-Intersection", 
            "Traffic Circle",
            "Roundabout", 
            "Five-Point, or More", 
            "L-Intersection", 
            "Other Intersection", 
            "Reported as Unknown"
            ], 
            # initialize the counts at zero
            "TotalDeaths": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            }

    # for loop through data counting each death for each intersection
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

    # compile and print death counts into a dataframe
    orgData = pd.DataFrame(totalDeathsPerIntersection)
    print(orgData)

    # create bar plot in normal scale
    plt.bar(orgData.Intersections, orgData.TotalDeaths)
    plt.xticks(rotation=90)
    plt.title("Total Fatalities at Given Intersections in 2020")
    plt.xlabel("Intersection Type")
    plt.ylabel("Fatals")
    plt.show()

    # create bar plot using log scale
    fig, ax = plt.subplots()
    plt.xticks(rotation=90)
    ax.bar(orgData.Intersections, orgData.TotalDeaths)
    plt.title("Total Fatalities at Given Intersections in 2020 (Log Scale)")
    ax.set_yscale('log')
    ax.set_xlabel("Intersection Type")
    ax.set_ylabel("Fatals")
    plt.show()

    # Calculate probability statistics based off of total fatalities
    totalFatals = sum(orgData.TotalDeaths)
    probabilities = {}
    other = 0
    for row_i in range(len(orgData.Intersections)):
        intersection = orgData.Intersections[row_i]
        deaths = int(orgData.TotalDeaths[row_i])
        prob = deaths/totalFatals
        calc = {"i": intersection, "p": prob}
        if prob > 0.05:
            probabilities[intersection] = prob
        else:
            other += prob
        probabilities["Other Intersections"] = other

        result = "Probability of death on %(i)s is %(p)s." % calc
        print(result)

    new_lst = [f'{i*100:.1f}%' for i in list(probabilities.values())]

    # plot a pie chart on probabilities
    plt.pie(list(probabilities.values()), labels=new_lst)
    plt.title("Probability of Deaths")
    plt.legend(list(probabilities.keys()), loc='upper right')
    plt.show()


if __name__ == "__main__":
    main()

# %%
