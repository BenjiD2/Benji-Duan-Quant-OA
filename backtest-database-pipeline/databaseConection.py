import datetime

from polygon import RESTClient

import pymysql
# import mysql.connector

def ts_to_datetime(ts) -> str:
    return datetime.datetime.fromtimestamp(ts / 1000.0).strftime('%Y-%m-%d %H:%M')

def main():
    key = "n20l_ZwmG_9ZvHv8IHtRi8a2A_Yi_IDh"

    connection=pymysql.connect (host='stock-database.c0ap9t2mxanj.us-east-2.rds.amazonaws.com',
                            user='admin',
                            password='abcd1234',
                            database='sys')

    cursor = connection.cursor()
    
    with RESTClient(key) as client:
        from_ = "2021-12-01"
        to = "2021-12-31"
        resp = client.stocks_equities_aggregates("AAPL", 1, "hour", from_, to, unadjusted=False, limit = 50000)

        #print(f"Hour aggregates for {resp.ticker} between {from_} and {to}.")
        # (Date, Name, c, h, l, n, o, t , v, vx)
        
        # (dt, "AAPL", {result['c']}, {result['h']}, {result['l']}, {result['n']}, {result['n']}, {result['o']}, {result['t']}, {result['v']}, {result['vx']},)
        for result in resp.results:
            dt = ts_to_datetime(result["t"])
            sql = ("""INSERT INTO Stocks (Date, Name, Close_Price, Highest_Price, Lowest_Price, Transactions, Open_Price, Trading_Volume, Volume_Weighted_Average_Price) 
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)""")
            cursor.execute(sql, (dt, "AAPL", {result['c']}, {result['h']}, {result['l']}, {result['t']}, {result['o']}, {result['v']}, {result['vw']}))
            connection.commit()
             #print(f"{dt}\n\tO: {result['o']}\n\tH: {result['h']}\n\tL: {result['l']}\n\tC: {result['c']} ")



# with connection:
#     cur = connection.cursor()
#     cur.execute("SELECT VERSION()")
#     version = cur.fetchone()
#     print("Database version: {} ".format(version[0]))

if __name__ == '__main__':
    main()

# print(mycursor.rowcount, "record inserted.")