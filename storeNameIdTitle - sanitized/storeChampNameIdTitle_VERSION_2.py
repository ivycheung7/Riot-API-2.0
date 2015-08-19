'''
Python script that requests data from Riot Server, then put it in a table

Data requested in this script:
    Champion ID
    Champion Name
    Champion Title

Edit: I could've used json to parse it >__< Will change this script if I have time later. At least it works
'''
#!/bin/usr/python
import requests
import re
import MySQLdb

API_KEY = <INSERT API KEY HERE>
SERVER = <INSERT SERVER HERE>
USER = <INSERT USER HERE>
PASSWORD = <INSERT PASSWORD HERE>
DATABASE = <INSERT DATABASE NAME HERE>
TABLE = <INSERT TABLE NAME HERE>

#Sends a request to get all the Champion name, ID and title first.
r = requests.get('https://na.api.pvp.net/api/lol/static-data/'+SERVER+'/v1.2/champion?api_key='+API_KEY)

#Retrive all the Champion names from the request using regular expression
name = re.findall(r'name":"(.*?)"',r.text)
ID = re.findall(r'id":(\d*)',r.text)
title = re.findall(r'title":"(.*?)"',r.text)

#Open database connection
database = MySQLdb.connect(<INSERT NETWORK HERE>, USER, PASSWORD, DATABASE)
#Prepare a cursor object using cursor method
cursor = database.cursor()

#Create the table if it doesn't exist already
sql = '''DROP TABLE IF EXISTS ''' + TABLE + ''';'''
cursor.execute(sql)
sql = '''CREATE TABLE ''' + TABLE + ''' (id int(3), name varchar(12), title varchar(32));'''
cursor.execute(sql)

#Insert into database, in the order of ID, Name and Title
for i in range(0,len(name)):
    sql = '''INSERT INTO ''' + TABLE + '''(id, name, title) VALUES ("%d", "%s", "%s")''' %(int(ID[i]), name[i], title[i])
    cursor.execute(sql)
    database.commit()

#Close database connection
database.close()
