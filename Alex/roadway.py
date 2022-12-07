import pandas as pd
data = pd.read_csv("accident.csv")
df = pd.DataFrame(data)
state_highway = df[df.STATE == 49][df.ROUTE == 3]
federal_highway = df[df.STATE == 49][df.ROUTE == 2]
interstate = df[df.STATE == 49][df.ROUTENAME == 1]
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