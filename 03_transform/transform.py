import pandas as pd
import sys

import_file = sys.argv[1]
export_file = sys.argv[2]

df = pd.read_csv(import_file)

df = df.iloc[:,:-1]

day = []
month = []
year = []
ratediff = []

for i in range(len(df.index)):
    d = df["UTCDate"][i].split(".")
    day.append(d[2])
    month.append(d[1])
    year.append(d[0])
     
    if df["whiteELO"][i] == "NA" or df["blackELO"][i] == "NA":
        ratediff.append("NA")
    else:
        ratediff.append(abs(df["whiteELO"][i] - df["blackELO"][i]))

df.insert(5, "day", day)
df.insert(6, "month", month)
df.insert(7, "year", year)
df.insert(11, "RatingDiff", ratediff)

df.to_csv(export_file, index = False, header = True)