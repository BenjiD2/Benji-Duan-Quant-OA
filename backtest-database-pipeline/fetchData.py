import mysql.connector

def fetchResult(a):
    # Input: Date (String)
    # Output: Stock Data
    # Accesses Amazon RDS using MySQL to search and return stock data at the given date
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
    # Input: None
    # Output: Stock Data
    # Accesses Amazon RDS using MySQL to return all stock data in the database
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