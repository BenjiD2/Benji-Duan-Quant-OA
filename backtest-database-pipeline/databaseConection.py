import datetime, pymysql, stockRetrieval
from polygon import RESTClient

def insertStockData(list):
    # Input: List of Stock containing hourly information
    # Output: None
    # Connects to Amazon RDS and inserts stock data into database
    connection=pymysql.connect (host='stock-database.c0ap9t2mxanj.us-east-2.rds.amazonaws.com',
                            user='admin',
                            password='abcd1234',
                            database='sys')
    cursor = connection.cursor()

    for stockInstance in list:
        sql = ("""INSERT INTO Stocks (Date, Name, Close_Price, Highest_Price, Lowest_Price, Transactions, Open_Price, Trading_Volume, Volume_Weighted_Average_Price) 
                 VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)""")
        cursor.execute(sql, (stockInstance.Date, stockInstance.Name, stockInstance.ClosePrice, stockInstance.HighestPrice, stockInstance.LowestPrice, stockInstance.Transactions, stockInstance.OpenPrice, stockInstance.TradingVolume, stockInstance.VolumeWeightedAverage))
        connection.commit()

def main():
    stockList = stockRetrieval.createListStock()
    insertStockData(stockList)
    
if __name__ == '__main__':
    main()