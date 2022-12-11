
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

# 1987-Later
# 1 Interstate
# 2 U.S. Highway
# 3 State Highway
# 4 County Road
# 5 Local Street – Township
# 6 Local Street – Municipality
# 7 Local Street – Frontage Road(Since 1994)
# 8 Other
# 9 Unknown


def getData(filename):
    data = pd.read_csv(filename, encoding_errors="replace")
    return data

def main():
    # get data from file
    filepath = "../data/FARS2020NationalCSV/accident.csv"
    accident2020 = getData(filepath)

    # create a frame to total death counts from each roadtypes
    totalDeathsPerRoadType = {
        "roadtypes": [
            "Interstate",
            "U.S. Highway",
            "State Highway",
            "County Road",
            "Local Street – Township",
            "Local Street – Municipality",
            "Local Street – Frontage Road",
            "Other",
            "Reported as Unknown"
            ], 
            # initialize the counts at zero
            "TotalDeaths": [0, 0, 0, 0, 0, 0, 0, 0, 0]
            }

    # for loop through data counting each death for each roadtypes
    roadtypeFatals = accident2020[["ROUTE", "FATALS"]]

    for i in range(len(roadtypeFatals)):
        if roadtypeFatals.ROUTE[i] == 1:
            roadtypeFatals.at[i, "ROUTE"] = "Interstate"
            totalDeathsPerRoadType["TotalDeaths"][0] += roadtypeFatals.at[i,"FATALS"]
        elif roadtypeFatals.ROUTE[i] == 2:
            roadtypeFatals.at[i, "ROUTE"] = "U.S. Highway"
            totalDeathsPerRoadType["TotalDeaths"][1] += roadtypeFatals.at[i, "FATALS"]
        elif roadtypeFatals.ROUTE[i] == 3:
            roadtypeFatals.at[i, "ROUTE"] = "State Highway"
            totalDeathsPerRoadType["TotalDeaths"][2] += roadtypeFatals.at[i, "FATALS"]
        elif roadtypeFatals.ROUTE[i] == 4:
            roadtypeFatals.at[i, "ROUTE"] = "County Road"
            totalDeathsPerRoadType["TotalDeaths"][3] += roadtypeFatals.at[i, "FATALS"]
        elif roadtypeFatals.ROUTE[i] == 5:
            roadtypeFatals.at[i, "ROUTE"] = "Local Street – Township"
            totalDeathsPerRoadType["TotalDeaths"][4] += roadtypeFatals.at[i, "FATALS"]
        elif roadtypeFatals.ROUTE[i] == 6:
            roadtypeFatals.at[i, "ROUTE"] = "Local Street – Municipality"
            totalDeathsPerRoadType["TotalDeaths"][5] += roadtypeFatals.at[i, "FATALS"]
        elif roadtypeFatals.ROUTE[i] == 7:
            roadtypeFatals.at[i,
                                  "ROUTE"] = "Local Street – Frontage Road"
            totalDeathsPerRoadType["TotalDeaths"][6] += roadtypeFatals.at[i, "FATALS"]
        elif roadtypeFatals.ROUTE[i] == 8:
            roadtypeFatals.at[i, "ROUTE"] = "Other"
            totalDeathsPerRoadType["TotalDeaths"][7] += roadtypeFatals.at[i, "FATALS"]
        else:
            roadtypeFatals.at[i, "ROUTE"] = "Reported as Unknown"
            totalDeathsPerRoadType["TotalDeaths"][8] += roadtypeFatals.at[i, "FATALS"]

    # compile and print death counts into a dataframe
    orgData = pd.DataFrame(totalDeathsPerRoadType)
    print(orgData)

    # create bar plot in normal scale
    plt.bar(orgData.roadtypes, orgData.TotalDeaths)
    plt.xticks(rotation=90)
    plt.title("Total Fatalities at Given Road Types in 2020")
    plt.xlabel("Road Type")
    plt.ylabel("Fatals")
    plt.show()

    # create bar plot using log scale
    fig, ax = plt.subplots()
    plt.xticks(rotation=90)
    ax.bar(orgData.roadtypes, orgData.TotalDeaths)
    plt.title("Total Fatalities at Given Road Types in 2020 (Log Scale)")
    ax.set_yscale('log')
    ax.set_xlabel("Road Type")
    ax.set_ylabel("Fatals")
    plt.show()

    # Calculate probability statistics based off of total fatalities
    totalFatals = sum(orgData.TotalDeaths)
    probabilities = {}
    other = 0
    for row_i in range(len(orgData.roadtypes)):
        roadtypes = orgData.roadtypes[row_i]
        deaths = int(orgData.TotalDeaths[row_i])
        prob = deaths/totalFatals
        calc = {"i": roadtypes, "p": prob}
        if prob > 0.05:
            probabilities[roadtypes] = prob
        else:
            other += prob
        probabilities["Other Road Types"] = other

        result = "Probability of death on %(i)s is %(p)s." % calc
        print(result)

    new_lst = [f'{i*100:.1f}%' for i in list(probabilities.values())]

    # plot a pie chart on probabilities
    plt.pie(list(probabilities.values()), labels=new_lst)
    plt.subplots_adjust(left=0.0, bottom=0.1, right=0.45)
    plt.title("Probability of Deaths")
    plt.legend(list(probabilities.keys()), 
                bbox_to_anchor=(1, 0.5), 
                loc="center right", 
                fontsize=10,
                bbox_transform=plt.gcf().transFigure)
    plt.show()


if __name__ == "__main__":
    main()

# %%
