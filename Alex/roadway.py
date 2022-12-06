import pandas as pd
data = pd.read_csv("accident.csv")
df = pd.DataFrame(data)
non_motorists = df.PEDS
motorists = df.PERSONS
state_highway = df[df.ROUTE == 3]
federal_highway = df[df.ROUTE == 2]
interstate = df[df.ROUTENAME == 1]
county_road = df[df.ROUTE == 4]
local_street_municipality = df[df.ROUTE == 6]
local_street_township = df[df.ROUTE == 5]
local_street_frontage_road = df[df.ROUTE == 7]
other_road = df[df.ROUTE == 8]
unknown = df[df.ROUTE == 9]