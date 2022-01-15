import mysql.connector

def fetchResult(a):
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
        record = cursor.fetchone()
        return(record)
        
    except mysql.connector.Error as error:
        print("Error while connecting to MySQL", error)

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

def fetchResults():
    try:
        connection = mysql.connector.connect(host='stock-database.c0ap9t2mxanj.us-east-2.rds.amazonaws.com',
                                             database='sys',
                                             user='admin',
                                             password='abcd1234')

        mySql_select_Query = "select * from Stocks"
        cursor = connection.cursor(buffered=True)
        cursor.execute(mySql_select_Query)
        record = cursor.fetchall()
        return(record)

    except mysql.connector.Error as error:
        print("Error while connecting to MySQL", error)

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()