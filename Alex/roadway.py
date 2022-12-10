import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv("accident2020.csv", encoding_errors='replace')
data1 = pd.read_csv("ACCIDENT2000.csv", encoding_errors='replace')
df = pd.DataFrame(data)
df1 = pd.DataFrame(data1)
#2020 data
state_highway = df[df.STATE == 49][df.ROUTE == 3]
federal_highway = df[df.STATE == 49][df.ROUTE == 2]
interstate = df[df.STATE == 49][df.ROUTE == 1]
county_road = df[df.STATE == 49][df.ROUTE == 4]
local_street_municipality = df[df.STATE == 49][df.ROUTE == 6]
local_street_township = df[df.STATE == 49][df.ROUTE == 5]
local_street_frontage_road = df[df.STATE == 49][df.ROUTE == 7]
other_road = df[df.STATE == 49][df.ROUTE == 8]
unknown = df[df.STATE == 49][df.ROUTE == 9]
motorists_state = state_highway.PERMVIT
motorists_federal = federal_highway.PERMVIT
motorists_interstate = interstate.PERMVIT
motorists_county = county_road.PERMVIT
motorists_municipality = local_street_municipality.PERMVIT
motorists_township = local_street_township.PERMVIT
motorists_frontage = local_street_frontage_road.PERMVIT
motorists_other = other_road.PERMVIT
motorists_unknown = unknown.PERMVIT
nonmotorists_state = state_highway.PERNOTMVIT
nonmotorists_federal = federal_highway.PERNOTMVIT
nonmotorists_interstate = interstate.PERNOTMVIT
nonmotorists_county = county_road.PERNOTMVIT
nonmotorists_municipality = local_street_municipality.PERNOTMVIT
nonmotorists_township = local_street_township.PERNOTMVIT
nonmotorists_frontage = local_street_frontage_road.PERNOTMVIT
nonmotorists_other = other_road.PERNOTMVIT
nonmotorists_unknown = unknown.PERNOTMVIT
#Make changes to the variables used to see bar graph results
plt.xticks(ticks = list(range(20)))
plt.yticks(ticks = list(range(20)))
plt.xlabel("Number of nonmotorists involved in crashes on unknown Utah roads")
plt.ylabel("Number of fatalities in crashes on unknown Utah roads")
plt.bar(nonmotorists_unknown, unknown.FATALS)