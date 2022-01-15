import datetime

from polygon import RESTClient

def ts_to_datetime(ts) -> str:
    return datetime.datetime.fromtimestamp(ts / 1000.0).strftime('%Y-%m-%d %H:%M')

class Stock:
    def __init__(self, date, name, close, high, low, trans, open, tvolume, vwaverage):
        self.Date = date 
        self.Name = name
        self.ClosePrice = close
        self.HighestPrice = high
        self.LowestPrice = low
        self.Transactions = trans
        self.OpenPrice = open
        self.TradingVolume = tvolume
        self.VolumeWeightedAverage = vwaverage

def result_to_Stock(result):
    dt = ts_to_datetime(result["t"])
    return Stock(dt, "AAPL", {result['c']}, {result['h']}, {result['l']}, {result['t']}, {result['o']}, {result['v']}, {result['vw']})

def listStock(from_ = "2021-12-01", to = "2021-12-31"):

    key = "n20l_ZwmG_9ZvHv8IHtRi8a2A_Yi_IDh"

    with RESTClient(key) as client:
        resp = client.stocks_equities_aggregates("AAPL", 1, "hour", from_, to, unadjusted=False, limit = 50000)
        stockList = []
        #print(f"Hour aggregates for {resp.ticker} between {from_} and {to}.")
        # (Date, Name, c, h, l, n, o, t , v, vx)
        
        # (dt, "AAPL", {result['c']}, {result['h']}, {result['l']}, {result['n']}, {result['n']}, {result['o']}, {result['t']}, {result['v']}, {result['vx']},)
        for result in resp.results:
            stockInterval = result_to_Stock(result)
            sql = ("""INSERT INTO Stocks (Date, Name, Close_Price, Highest_Price, Lowest_Price, Transactions, Open_Price, Trading_Volume, Volume_Weighted_Average_Price) 
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)""")
            # stockInterval = Stock((dt, "AAPL", {result['c']}, {result['h']}, {result['l']}, {result['t']}, {result['o']}, {result['v']}, {result['vw']}))
            stockList.append(stockInterval)

    return stockList

if __name__ == '__main__':
    bigStock = listStock()
    print(bigStock)