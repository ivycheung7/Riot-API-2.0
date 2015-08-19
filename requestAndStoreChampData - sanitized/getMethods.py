'''
This is a module to access the match information when json is turned into a dictionary
'''

import logging #To just note down all of the matchIds and their errors, then fix it later

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
    logging.basicConfig(filename='exceptions.log', level=logging.DEBUG) #Made a log file for all the exceptions
    bannedChampList = [] #To put champ Ids in and return it
    try:
        teamBansList =  matchDataDict['teams'][index]['bans'] #Returns a list of 3 dictionaries, each with pick turn and banned champ
        if len(teamBansList) < 3: #Logging to see if some teams only have 1 or 2 bans
            logging.debug('This ban list is the len of '+ len(teamBansList) + ', teamId = ' +matchDataDict['matchId'])
        for bans in teamBansList:
            bannedChampList.append(bans['championId']) #Adds the champion Id to the ban list
    except Exception, e: #Throws exceptions, log them, and then debug them later
        logging.info(matchDataDict['matchId'])
        logging.warning('teamId ' + matchDataDict['teamId'] + 'does not have a ban section')
        logging.exception(e)
    return bannedChampList
