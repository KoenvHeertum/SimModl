# POTENTIEEL NOG TABULATE INSTALLEREN!   pip install tabulate
import random
import numpy as np
from tabulate import tabulate
#teams: AJX - FEY - PSV - FCU - WIL

# Mijn vrij simpele Random Number Generator. Verreweg van perfect.
def RNGsim(maxNumber):
    startInt = random.randint(4, 100) # om een willekeurig startgetal te hebben.
    squareInt = startInt**2
    actualInt = str(squareInt)[1:3]
    return int(actualInt)

# Bevat een dictionary met alle mogelijke wedstrijden en hun kansen, heeft een matchString nodig (bijv. FEYAJX).
# Returned de percentages die bij de wedstrijd horen, en stuurt de dictionary door voor de matchStrings.
def percentages(key):
    dict = {
        "AJXFEY": "65, 17, 18",
        "AJXPSV": "54, 21, 25",
        "AJXFCU": "74, 14, 12",
        "AJXWIL": "78, 13, 09",
        "FEYAJX": "30, 21, 49",
        "FEYPSV": "37, 24, 39",
        "FEYFCU": "51, 22, 27",
        "FEYWIL": "60, 21, 19",
        "PSVAJX": "39, 22, 39",
        "PSVFEY": "54, 22, 24",
        "PSVFCU": "62, 20, 18",
        "PSVWIL": "62, 22, 16",
        "FCUAJX": "25, 14, 61",
        "FCUFEY": "37, 23, 40",
        "FCUPSV": "29, 24, 47",
        "FCUWIL": "52, 23, 25",
        "WILAJX": "17, 18, 65",
        "WILFEY": "20, 26, 54",
        "WILPSV": "23, 24, 53",
        "WILFCU": "37, 25, 38"
    }
    win = dict[key][0:2]
    tie = dict[key][4:6]
    lose = dict[key][8:10]
    return win, tie, lose, dict

# Beslist de winnaar, gebaseerd op de kansen. Stuurt de punten (3 voor win, 1 gelijk, 0 verlies) door in home-, away-team format.
def decideWinner(win, tie, lose):
    home = 0
    away = 0
    randNr = RNGsim(100)
    if randNr <= int(win):
        home += 3
    elif randNr <= int(win) + int(tie):
        home += 1
        away += 1
    else:
        away += 3
    return home, away

# Geeft de verdiende competitiepunten mee aan de teams die gespeeld hebben
def playMatch(matchString):
    hTeam = matchString[0:3]
    aTeam = matchString[3:6]
    win, tie, lose, dicti = percentages(matchString)
    points = decideWinner(win, tie, lose)
    hPoints = points[0]
    aPoints = points[1]
    return hTeam, hPoints, aTeam, aPoints
    
# Doet playMatch voor alle mogelijke wedstrijden. Returned een dictionary met de verdiende punten per team.    
def playCompetition():
    dict =  percentages("FCUWIL")[3] #nodig om de dictionary op te vragen, hierdoor hoef ik niet alle matchStrings te kopiëren.
    AJX = 0
    FEY = 0
    PSV = 0
    FCU = 0
    WIL = 0
    matches = []
    for key in dict:
        matches.append(key)
    # Dit kon mooier, maar het werkt.
    for matchStr in matches:
        playedM = playMatch(matchStr)
        if(playedM[0]) == "AJX":
            AJX += playedM[1]
        elif(playedM[2]) == "AJX":
            AJX += playedM[3]
        if(playedM[0]) == "FEY":
            FEY += playedM[1]
        elif(playedM[2]) == "FEY":
            FEY += playedM[3]
        if(playedM[0]) == "PSV":
            PSV += playedM[1]
        elif(playedM[2]) == "PSV":
            PSV += playedM[3]
        if(playedM[0]) == "FCU":
            FCU += playedM[1]
        elif(playedM[2]) == "FCU":
            FCU += playedM[3]
        if(playedM[0]) == "WIL":
            WIL += playedM[1]
        elif(playedM[2]) == "WIL":
            WIL += playedM[3]
    
    standings = {
        "AJX": AJX,
        "FEY": FEY,
        "PSV": PSV,
        "FCU": FCU,
        "WIL": WIL
    }
    return(standings)

# Zet de teams in stand-volgorde in een lijst. Index is de positie in de competitie. #1 op index 0, #2 op index 1 etc.
def checkStandings():
    dictionary = playCompetition()
    dictionary = {k: v for k, v in sorted(dictionary.items(), key=lambda item: item[1], reverse=True)}
    # Source: https://stackoverflow.com/questions/613183/how-do-i-sort-a-dictionary-by-value
    standingsList = []
    for item in dictionary:
        standingsList.append(item)
    return(standingsList)
        
# Berekent de percentages en maakt de matrix/tabel (via Tabulate)
def createMatrix(amountOfRuns):
    AJX = []
    FEY = []
    PSV = []
    FCU = []
    WIL = []
    
    # Append de ranking (#1, #2 etc) naar een lijst, maakt het makkelijker om mee te rekenen
    for i in range(0, amountOfRuns):
        run = checkStandings()
        AJX.append(run.index("AJX")+1)
        FEY.append(run.index("FEY")+1)
        PSV.append(run.index("PSV")+1)
        FCU.append(run.index("FCU")+1)
        WIL.append(run.index("WIL")+1)
    
    AJXper = []
    FEYper = []
    PSVper = []
    FCUper = []
    WILper = []
    
    # Berekent de percentages van alle rankings door ze te delen door de runs.
    for index in range(1, 6):
        AJXper.append((AJX.count(index) / amountOfRuns)*100)
        FEYper.append((FEY.count(index) / amountOfRuns)*100)
        PSVper.append((PSV.count(index) / amountOfRuns)*100)
        FCUper.append((FCU.count(index) / amountOfRuns)*100)
        WILper.append((WIL.count(index) / amountOfRuns)*100)
    
    # Maakt de matrix via tabulate (zodat het er mooier uit ziet)
    matrix = np.array([["Ajax", AJXper[0], AJXper[1], AJXper[2], AJXper[3], AJXper[4]],
                        ["Feyenoord", FEYper[0], FEYper[1], FEYper[2], FEYper[3], FEYper[4]],
                        ["PSV", PSVper[0], PSVper[1], PSVper[2], PSVper[3], PSVper[4]],
                        ["FC Utrecht", FCUper[0], FCUper[1], FCUper[2], FCUper[3], FCUper[4]],
                        ["Willem II", WILper[0], WILper[1], WILper[2], WILper[3], WILper[4]]])
    headers = ["in %", "#1", "#2", "#3", "#4", "#5"]
    table = tabulate(matrix, headers, tablefmt='fancy_grid')
    print(table)

# De enige functie die wordt gerunned
createMatrix(1000)
