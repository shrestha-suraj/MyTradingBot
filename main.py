import threading,sys
sys.path.append('./src')
from trading import *
from stockdata import *
from config import *


# This is the main function that will carry out all the processes
def start_module(stock_dict):
    for stock in stock_dict:
        try:
            # current_stock_monitor[stock]=float(stockData(stock)['1. open'])
            print(stock)
            current_price=stockData('IBM')['1. open']
            print(current_price)
        except:
            print("Stock not found.")
    # print(current_stock_monitor)
    # t=threading.Timer(60.00,start_module,args=(stocks,))
    # t.start()

def main():
    # This variable holds my buying power
    buying_power=float(accountDetails()['buying_power'])
    print("Your Buying Power is: "+str(buying_power))
    each_buying_power=buying_power/5
    # Here I will need the five stocks that I will be targeting
    stocks=top_gainers()
    stock_dict={}
    for stock in stocks:
        stock_dict[stock]=stock_analysis(stock)
    print(stock_dict)
    start_module(stock_dict)

def stock_analysis(stockTicker):
    BASE_URL="https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={}&interval=1min&apikey={}".format(stockTicker,ALPHAVANTAGE_API_KEY_ONE)
    result=requests.get(BASE_URL)
    result=json.loads(result.content)['Time Series (Daily)'].values()
    highAverage=0
    lowAverage=0
    totalData=len(result)
    for each in result:
        highAverage+=float(each['2. high'])
        lowAverage+=float(each['3. low'])
    return {'low':round(lowAverage/totalData,4),'high':round(highAverage/totalData,4)}


main()
# print(stockData('FOCS')['1. open'])
