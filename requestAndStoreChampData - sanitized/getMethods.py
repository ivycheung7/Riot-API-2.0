'''
This is a module to access the match information when json is turned into a dictionary
'''

def getChampionId(matchDataDict, index):
    '''Returns championId from dictionary as an int'''
    return matchDataDict['participants'][index]['championId']

def getWardsPlaced(matchDataDict, index):
    '''Returns wardsPlaced from dictionary as an int'''
    return matchDataDict['participants'][index]['stats']['wardsPlaced']

def getWinnerPlayer(matchDataDict, index):
    '''Returns True if won, otherwise False, as boolean'''
    return matchDataDict['participants'][index]['stats']['winner']

def getBannedChampId(matchDataDict, index):
    '''Return a list of banned champion Id made by team 1 or team 2, depending on index'''
    bannedChampList = [] #To put champ Ids in and return it
    teamBansList =  matchDataDict['teams'][index]['bans'] #Returns a list of 3 dictionaries, each with pick turn and banned champ
    for bans in teamBansList:
        bannedChampList.append(bans['championId']) #Adds the champion Id to the ban list
    return bannedChampList
