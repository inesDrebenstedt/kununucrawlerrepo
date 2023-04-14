# import the mysql client for python

import pymysql

def createAndConnectDB():

    # Create a connection object
    # IP address of the MySQL database server
    Host = "localhost"

    # User name of the database server
    User = "user"

    # Password for the database user
    Password = ""

    conn = pymysql.connect(host=Host, user=User, password=Password)

    # Create a cursor object
    cur = conn.cursor()

    # creating database
    cur.execute("CREATE DATABASE kununuratings")

    cur.execute("SHOW DATABASES")
    databaseList = cur.fetchall()

    for database in databaseList:
        print(database)

    conn.close()

def createTable():
    conn = pymysql.connect('localhost', 'user', 'password', 'kununuratings')
    cur = conn.cursor()
    cur.execute("DROP TABLE IF EXISTS COWORKER_RATINGS")
    createCoworkerRatingsTableQuery = """
             CREATE TABLE COWORKER_RATINGS ( 
             RATING_ID  CHAR(20) NOT NULL, 
             COMPANY_NAME VARCHAR(64) NOT NULL,
             xData  int(10), 
             yData int(10) 
             """

    # To execute the SQL query
    cur.execute(createCoworkerRatingsTableQuery)

    # To commit the changes
    conn.commit()
    conn.close()
