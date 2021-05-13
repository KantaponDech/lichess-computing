import re
import pandas as pd
import sys

import_file = sys.argv[1]
export_file = sys.argv[2]

with open(import_file, 'r') as file:
    data = file.readlines()
file.close()

event = []
white = []
black = []
result = []
UTCDate = []
UTCTime =[]
whiteELO = []
blackELO = []
whiteRatingDiff = []
blackRatingDiff = []
ECO = []
opening = []
timeControl = []
termination = []
totalMove = []
AN = []

for line in range(len(data)):
    a = re.findall(r"^\[Event \"(.*)\"\]", data[line])
    b = re.findall(r"^\[White \"(.*)\"\]", data[line])
    c = re.findall(r"^\[Black \"(.*)\"\]", data[line])
    d = re.findall(r"^\[Result \"(.*)\"\]", data[line])
    e = re.findall(r"^\[UTCDate \"(.*)\"\]", data[line])
    f = re.findall(r"^\[UTCTime \"(.*)\"\]", data[line])
    g = re.findall(r"^\[WhiteElo \"(.*)\"\]", data[line])
    h = re.findall(r"^\[BlackElo \"(.*)\"\]", data[line])
    i = re.findall(r"^\[WhiteRatingDiff \"(.*)\"\]", data[line])
    j = re.findall(r"^\[BlackRatingDiff \"(.*)\"\]", data[line])
    k = re.findall(r"^\[ECO \"(.*)\"\]", data[line])
    l = re.findall(r"^\[Opening \"(.*)\"\]", data[line])
    m = re.findall(r"^\[TimeControl \"(.*)\"\]", data[line])
    n = re.findall(r"^\[Termination \"(.*)\"\]", data[line])
    o = re.findall(r"^1\..*", data[line])

    if len(a) != 0: event.append(a)
    elif len(b) != 0: white.append(b)
    elif len(c) != 0: black.append(c)
    elif len(d) != 0: result.append(d)
    elif len(e) != 0: UTCDate.append(e)
    elif len(f) != 0: UTCTime.append(f)

    elif len(g) != 0: # Avoid Unknwon Rating
        if g == ["?"] or len(re.findall(r"^\[WhiteRatingDiff \"(.*)\"\]", data[line + 2])) == 0:
            whiteELO.append(g)
            whiteRatingDiff.append(["NA"])
            blackRatingDiff.append(["NA"])
        else:
            whiteELO.append(g)
    elif len(h) != 0: # Avoid Unknwon Rating
        if h == ["?"] or len(re.findall(r"^\[BlackRatingDiff \"(.*)\"\]", data[line + 2])) == 0:
            blackELO.append(h)
            if len(blackELO) != len(whiteRatingDiff):
                whiteRatingDiff.append(["NA"])
                blackRatingDiff.append(["NA"])
        else:
            blackELO.append(h)

    elif len(i) != 0: whiteRatingDiff.append(i)
    elif len(j) != 0: blackRatingDiff.append(j)
    elif len(k) != 0: ECO.append(k)
    elif len(l) != 0: opening.append(l)
    elif len(m) != 0: timeControl.append(m)
    elif len(n) != 0: termination.append(n)
    
    if len(o) == 0: # Avoid not move in each game
        o = re.findall(r"\s(1-0|0-1|1/2-1/2)", data[line])
        if len(o) != 0: AN.append(["0."])
    elif len(o) != 0: AN.append(o)

for i in range(len(AN)): # Find total move in each game
    inserter = re.findall(r"([0-9]+)\.[^0-9]", str(AN[i]))
    totalMove.append(inserter[-1:])

event = [item for sublist in event for item in sublist]
white = [item for sublist in white for item in sublist]
black = [item for sublist in black for item in sublist]
result = [item for sublist in result for item in sublist]
UTCDate = [item for sublist in UTCDate for item in sublist]
UTCTime = [item for sublist in UTCTime for item in sublist]
whiteELO = [item for sublist in whiteELO for item in sublist]
blackELO = [item for sublist in blackELO for item in sublist]
whiteRatingDiff = [item for sublist in whiteRatingDiff for item in sublist]
blackRatingDiff = [item for sublist in blackRatingDiff for item in sublist]
ECO = [item for sublist in ECO for item in sublist]
opening = [item for sublist in opening for item in sublist]
timeControl = [item for sublist in timeControl for item in sublist]
termination = [item for sublist in termination for item in sublist]
totalMove = [item for sublist in totalMove for item in sublist]
AN = [item for sublist in AN for item in sublist]

for i in range(len(event)):
    replacer = re.findall(r"tournament (.*)", event[i])
    if len(replacer) != 0:
	    event[i] = (event[i].replace(replacer[0], "")).strip()

df = pd.DataFrame()

df["event"] = event
df["white"] = white
df["black"] = black
df["result"] = result
df["UTCDate"] = UTCDate
df["UTCTime"] = UTCTime
df["whiteELO"] = whiteELO
df["blackELO"] = blackELO
df["whiteRatingDiff"] = whiteRatingDiff
df["blackRatingDiff"] = blackRatingDiff
df["ECO"] = ECO
df["opening"] = opening
df["timeControl"] = timeControl
df["termination"] = termination
df["totalMove"] = totalMove
df["AN"] = AN

df.to_csv(export_file, index = False, header = True)