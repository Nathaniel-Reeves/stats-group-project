import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv("accident2020.csv", encoding_errors='replace')
df = pd.DataFrame(data)
county_owned = df[df.STATE == 49][df.RD_OWNER == 2]
state_owned = df[df.STATE == 49][df.RD_OWNER == 1]
federal_owned = df[df.STATE == 49][df.RD_OWNER == 60]
private_owned = df[df.STATE == 49][df.RD_OWNER == 26]
plt.xticks(ticks = list(range(20)))
plt.yticks(ticks = list(range(0, 2000, 20)))
plt.xlabel("Number of fatalities in a crash on privately owned roads in Utah")
plt.ylabel("Number of crashes involving the specific number of privately on federally owned roads in Utah")
plt.hist(private_owned.FATALS)