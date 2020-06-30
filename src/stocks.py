import requests, json
from bs4 import BeautifulSoup
from config import ALPACA_API_KEY,ALPACA_SECRET_KEY

# This function returns the top 5 stock gainers of the day
def top_five_gainers():
    stocks=[]
    BASE_URL="https://finance.yahoo.com/gainers" 
    response=requests.get(BASE_URL)
    web_content=response.content
    soup=BeautifulSoup(web_content,'html.parser')
    symbols=soup.findAll('a',{'class':'Fw(600)'})[:5]
    for each in symbols:
        for one in each:
            stocks.append(one.replace("-","."))
    return stocks


# This function retunrns the stock data of each min of the market
def each_minute_data(stockTicker):
    BASE_URL="https://data.alpaca.markets"
    HEADER_DATA={"APCA-API-KEY-ID":ALPACA_API_KEY,"APCA-API-SECRET-KEY":ALPACA_SECRET_KEY}
    LAST_TRADE_URL="{}/v1/last/stocks/{}".format(BASE_URL,stockTicker)
    result=requests.get(LAST_TRADE_URL,headers=HEADER_DATA)
    return json.loads(result.content)['last']['price']



def buy_sell_range(stockTicker,api_key_two):
    BASE_URL="https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={}&interval=1min&apikey={}".format(stockTicker,api_key_two)
    result=requests.get(BASE_URL)
    result=json.loads(result.content)['Time Series (Daily)'].values()
    highAverage=0
    lowAverage=0
    totalData=len(result)
    for each in result:
        highAverage+=float(each['2. high'])
        lowAverage+=float(each['3. low'])
    return {'low':round(lowAverage/totalData,4),'high':round(highAverage/totalData,4)}


# print(result["2020-06-19 16:00:00"])
# Above statement prints the below statement
# {'1. open': '1000.1100', '2. high': '1000.9590', '3. low': '999.7800', '4. close': '1000.5700', '5. volume': '78787'}