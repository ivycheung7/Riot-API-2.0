'''
Python script that requests data from Riot Server, then put it in a table

Data requested in this script:
    Champion ID
    Champion Name
    Champion Title

Edit: Could've used json >__< Will edit script later when I have time
'''
#!/bin/usr/python
import requests
import re
import MySQLdb

#Sends a request to get all the Champion name, ID and title first.
r = requests.get('https://na.api.pvp.net/api/lol/static-data/na/v1.2/champion?api_key=<INSERT KEY HERE>')

#Retrive all the Champion names from the request using regular expression
name = re.findall(r'name":"(.*?)"',r.text)
ID = re.findall(r'id":(\d*)',r.text)
title = re.findall(r'title":"(.*?)"',r.text)

#Open database connection
database = MySQLdb.connect("<INSERT NETWORK HERE>", "<INSERT USER>", "<INSERT PASSWORD>", "<INSERT DATABASE NAME>")
#Prepare a cursor object using cursor method
cursor = database.cursor()

for i in range(0,len(name)):
    sql = '''INSERT INTO <INSERT DATABASE NAME HERE> (name, id, title) VALUES ("%s", "%d", "%s")''' %(name[i], int(ID[i]), title[i])
    cursor.execute(sql)
    database.commit()
#print "Database version: %s " %data

#Close database connection
database.close()
