# import the mysql client for python

import pymysql
import mysql.connector

def createAndConnectDB(DataBaseName):

    # Create a connection object
    # IP address of the MySQL database server
    Host = "localhost"

    # User name of the database server
    User = "new_user"

    # Password for the database user
    Password = "Password_2023"

    conn = mysql.connector.connect(host=Host, user=User, password=Password)

    # Create a cursor object
    cur = conn.cursor()

    # creating database
    cur.execute("CREATE DATABASE IF NOT EXISTS kununuratings")

    cur.execute("SHOW DATABASES")
    databaseList = cur.fetchall()

    for database in databaseList:
        print('DATABASE in SYSTEM: ', database)

    createTable(conn, cur, 'kununuratings')

    conn.close()

def createTable(conn, cur, databaseName):
    #conn = pymysql.connect('localhost', 'user', 'password', 'kununuratings')
    #cur = conn.cursor()
    useDBCommand = 'USE ' + databaseName
    cur.execute(useDBCommand)
    cur.execute("DROP TABLE IF EXISTS COWORKER_RATINGS")
    createCoworkerRatingsTableQuery = """
             CREATE TABLE COWORKER_RATINGS ( 
             RATING_ID  int(10) NOT NULL AUTO_INCREMENT PRIMARY_KEY, 
             COMPANY_NAME VARCHAR(64) NOT NULL,
             xData  DOUBLE NULL DEFAULT NULL, 
             yData DOUBLE NULL DEFAULT NULL)
             """

    # To execute the SQL query
    cur.execute(createCoworkerRatingsTableQuery)

    # To commit the changes
    conn.commit()
    #conn.close()
