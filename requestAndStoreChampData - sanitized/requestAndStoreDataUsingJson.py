'''
Python script that requests data from Riot Server, then put them in a table

Data requested in this script:
    Champion ID
    Number of Times Picked
    Number of Times Banned
    Number of Times Won
    Number of Times Warded

Questions to be answered with data collectd:
    Champion picked rate?
    Champion banned rate?
    Champion win rate?
    Champion ward rate?

    Champion ban rate vs win rate
    Champion ward rate vs win rate
'''
import requests
import json
import getMethods #A module I wrote myself for all get methods for the dictionary
from updateDatabase import updateDatabase #A module I wrote myself for all update database methods

#Puting all sensitive information here so I can delete them easily later. They shouldn't change
API_KEY = <API KEY HERE>
SERVER = <SERVER HERE>
TABLE = <TABLE NAME HERE> #Name of the table you want to update

def requestData(matchId, SERVER, API_KEY):
    '''Sends request to API and retrieve the response. Then convert json and return a dictionary'''
    url = 'https://na.api.pvp.net/api/lol/' + SERVER + '/v2.2/match/' + matchId + '?api_key=' + API_KEY
    r = requests.get(url)
    #print r #For testing purposes
    jsonDict = json.loads(r.text)
    return jsonDict

def getAndStoreData(matchDataDict):
    '''Opens database, update information, and close connection. Tables are pre-made already with necessary columns'''
    #Finding out champion pick rate, win rate and ward rate
    for index in range (0, 10): #Because I know for a fact there are 10 players in a game
        champId = getMethods.getChampionId(matchDataDict, index) #gets championId from dictionary
        wardsPlaced = getMethods.getWardsPlaced(matchDataDict, index) #gets wardsPlaced from dictionary
        updateDatabase(TABLE, <COLUMN NAME HERE>, champId) #Update database with +1 for picked for that champion
        updateDatabase(TABLE, <COLUMN NAME HERE>, champId, wardsPlaced) #Update database, adding to existing number of wards
        if getMethods.getWinnerPlayer(matchDataDict, index): #If True, because function returns boolean
            updateDatabase(TABLE, <COLUMN NAME HERE>, champId)
    for index in range (0, 2): #Because I know there are 2 teams in this game
        bannedChampList = getMethods.getBannedChampId(matchDataDict, index)
        for bannedChampId in bannedChampList:
            updateDatabase(TABLE, <COLUMN NAME HERE>, bannedChampId)

def main():
    matchDataDict = requestData(matchId, SERVER, API_KEY)
    getAndStoreData(matchDataDict)

main()
