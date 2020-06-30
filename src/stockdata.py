import requests, json
from bs4 import BeautifulSoup
from config import *

# This function retunrns the stock data of each min of the market
def stockData(stockTicker):
    BASE_URL="https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={}&interval=1min&apikey={}".format(stockTicker,ALPHAVANTAGE_API_KEY_TWO)
    result=requests.get(BASE_URL)
    print("Stock data triggered")
    result=json.loads(result.content)['Time Series (1min)']
    values_view=result.values()
    value_iterator=iter(values_view)
    # Current stock price and details each min price
    return next(value_iterator)

# This function returns the top 5 stock gainers of the day
def top_gainers():
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

# print(result["2020-06-19 16:00:00"])
# Above statement prints the below statement
# {'1. open': '1000.1100', '2. high': '1000.9590', '3. low': '999.7800', '4. close': '1000.5700', '5. volume': '78787'}