'''
This is a module with functions to update columns in the database
'''
import MySQLdb

def updateDatabase(tableName, columnName, champId, increment = 1):
    '''
    Adds certain amount to your specified table and column with an increment of default 1
    Only works in columns that specifically has int values.
    default increment is 1, you can pass in an extra parameter to change it
    sql = 'UPDATE tableName SET columnName = columnName+increment WHERE id = champId'
    '''
    #Putting important information here because I don't want to have more parameters
    NETWORK = <INSERT NETWORK HERE>
    USER = <INSERT USER HERE>
    PASSWORD = <INSERT PASSWORD HERE>
    DATABASE = <INSERT DATABASE NAME HERE>
    database = MySQLdb.connect(NETWORK, USER, PASSWORD, DATABASE) #Connects to database
    cursor = database.cursor() #Creates a cursor object because it's necessary
    ########################################################################################
    sql = 'UPDATE ' + tableName + ' SET ' + columnName + '=' + columnName + '+' + str(increment) + ' WHERE id = ' + str(champId) + ';'
    cursor.execute(sql) #Execute the above concatenated line of sql
    database.commit() #Has to commit, or no change will appear
    database.close() #Close database

def resetDatabaseData(tableName):
    NETWORK = <INSERT NETWORK HERE>
    USER = <INSERT USER HERE>
    PASSWORD = <INSERT PASSWORD HERE>
    DATABASE = <INSERT DATABASE NAME HERE>
    database = MySQLdb.connect(NETWORK, USER, PASSWORD, DATABASE) #Connects to database
    cursor = database.cursor() #Creates a cursor object because it's necessary
    #########################################################################################
    columnsToReset = [<INSERT ALL THE COLUMNS THAT YOU WANT TO RESET TO ZERO>]
    for column in columnsToReset:
        sql = 'UPDATE ' + tableName + ' SET ' + column + '=0;'
        cursor.execute(sql) #Execute the above concatenated line of sql
        database.commit()
    database.close()
