import mysql.connector

row = 200

def fetchResults(a):
    try:
        connection = mysql.connector.connect(host='stock-database.c0ap9t2mxanj.us-east-2.rds.amazonaws.com',
                                             database='sys',
                                             user='admin',
                                             password='abcd1234')

        current = str(a)
        
        mySql_select_Query = ("Select * from Stocks WHERE Date = %s")
        Date = (current,)
        cursor = connection.cursor(buffered=True)
        cursor.execute(mySql_select_Query, Date)
    # for k in range (0, row):
        record = cursor.fetchone()
        
    # record = cursor.execute("SELECT * from Stocks")
        return(record)
    # WHERE Date = '2021-12-01 12:00'
    except mysql.connector.Error as error:
        print("Error while connecting to MySQL", error)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

def fetchResult():
    try:
        connection = mysql.connector.connect(host='stock-database.c0ap9t2mxanj.us-east-2.rds.amazonaws.com',
                                             database='sys',
                                             user='admin',
                                             password='abcd1234')

        mySql_select_Query = "select * from Stocks"
        cursor = connection.cursor(buffered=True)
        cursor.execute(mySql_select_Query)
    # for k in range (0, row):
        record = cursor.fetchall()
    # record = cursor.execute("SELECT * from Stocks")
        print(record)

    # WHERE Date = '2021-12-01 12:00'
    except mysql.connector.Error as error:
        print("Error while connecting to MySQL", error)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")