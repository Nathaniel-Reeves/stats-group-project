import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv("data/FARS2020NationalCSV/ACCIDENT.csv", encoding_errors='replace')
data1 = pd.read_csv("data/FARS2000NationalCSV/ACCIDENT.CSV", encoding_errors='replace')
df = pd.DataFrame(data)
df1 = pd.DataFrame(data1)
state_highway = df[df.STATE == 49][df.ROUTE == 3]
federal_highway = df[df.STATE == 49][df.ROUTE == 2]
interstate = df[df.STATE == 49][df.ROUTE == 1]
county_road = df[df.STATE == 49][df.ROUTE == 4]
local_street_municipality = df[df.STATE == 49][df.ROUTE == 6]
local_street_township = df[df.STATE == 49][df.ROUTE == 5]
local_street_frontage_road = df[df.STATE == 49][df.ROUTE == 7]
other_road = df[df.STATE == 49][df.ROUTE == 8]
unknown = df[df.STATE == 49][df.ROUTE == 9]
motorists_state = state_highway.PERSONS
motorists_federal = federal_highway.PERSONS
motorists_interstate = interstate.PERSONS
motorists_county = county_road.PERSONS
motorists_municipality = local_street_municipality.PERSONS
motorists_township = local_street_township.PERSONS
motorists_frontage = local_street_frontage_road.PERSONS
motorists_other = other_road.PERSONS
motorists_unknown = unknown.PERSONS
nonmotorists_state = state_highway.PEDS
nonmotorists_federal = federal_highway.PEDS
nonmotorists_interstate = interstate.PEDS
nonmotorists_county = county_road.PEDS
nonmotorists_municipality = local_street_municipality.PEDS
nonmotorists_township = local_street_township.PEDS
nonmotorists_frontage = local_street_frontage_road.PEDS
nonmotorists_other = other_road.PEDS
nonmotorists_unknown = unknown.PEDS
#Make changes to the variables used to see bar graph results
plt.xlabel("Number of nonmotorists involved in crashes on unknown Utah roads")
plt.ylabel("Number of fatalities in crashes on unknown Utah roads")
plt.bar(nonmotorists_unknown, unknown.FATALS)