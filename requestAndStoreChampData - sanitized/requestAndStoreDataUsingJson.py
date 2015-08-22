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
from time import sleep #To pause the program when response 429 comes up
import requests
import json
import getMethods #A module I wrote myself for all get methods for the dictionary
from updateDatabase import updateDatabase #A module I wrote myself for all update database methods

#Puting all sensitive information here so I can delete them easily later. They shouldn't change
API_KEY = <INSERT API KEY HERE>
SERVER = <INSERT SERVER HERE>
TABLE = <INSERT TABLE NAME HERE> #Name of the table you want to update

def requestData(matchId, SERVER, API_KEY):
    '''Sends request to API and retrieve the response. Then convert json and return a dictionary'''
    url = 'https://na.api.pvp.net/api/lol/' + SERVER + '/v2.2/match/' + str(matchId) + '?api_key=' + API_KEY
    r = requests.get(url)
    while r.status_code != 200: #Because response 429 happens way too often
        print r.status_code
        sleep(5) #Wait 10 seconds and try again
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
        updateDatabase(TABLE, 'picked', champId) #Update database with +1 for picked for that champion
        updateDatabase(TABLE, 'warded', champId, wardsPlaced) #Update database, adding to existing number of wards
        if getMethods.getWinnerPlayer(matchDataDict, index): #If True, because function returns boolean
            updateDatabase(TABLE, 'won', champId)
    for index in range (0, 2): #Because I know there are 2 teams in this game
        bannedChampList = getMethods.getBannedChampId(matchDataDict, index)
        for bannedChampId in bannedChampList:
            updateDatabase(TABLE, 'banned', bannedChampId)

def main():
    #Open the file with all the match IDs
    jsonFile = open(jsonFilePath)
    #Take all the content out of the file
    jsonContent = jsonFile.read()
    #Get all the matchId and put it in a list
    allMatchId = json.loads(jsonContent)
    for matchId in allMatchId:
        matchDataDict = requestData(matchId, SERVER, API_KEY)
        getAndStoreData(matchDataDict)
    jsonFile.close()

main()
