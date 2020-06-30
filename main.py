import threading,sys
sys.path.append('./src')
from trading import *
from stockdata import *
from decimal import *
getcontext().prec=4

# This function is responsible to run a threading function every 15 seconds or as per user set
def set_interval(my_function,interval):
    def function_wrapper():
        set_interval(my_function,interval)
        my_function()
    t=threading.Timer(interval,function_wrapper)
    t.start()
    return t

# This is the main function that will carry out all the processes
def start_module(stock_dict):
    # current_stock_monitor={}
    all_stocks=[]
    all_prices=[]
    for stock in stock_dict:
        print(stock)
        try:
            # current_stock_monitor[stock]=float(stockData(stock)['1. open'])
            all_prices.append(float(stockData(stock)['1. open']))
            all_stocks.append(stock)
        except:
            print("Stock not found.")
    print(all_stocks)
    print(all_prices)
    # print(current_stock_monitor)
    # t=threading.Timer(60.00,start_module,args=(stocks,))
    # t.start()

def main():
    # This variable holds my buying power
    buying_power=float(accountDetails()['buying_power'])
    each_buying_power=buying_power/5
    # Here I will need the five stocks that I will be targeting
    stocks=top_gainers()
    stock_dict={}
    for stock in stocks:
        stock_dict[stock]=stock_analysis(stock)
    start_module(stock_dict)

def stock_analysis(stockTicker):
    BASE_URL="https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={}&interval=1min&apikey={}".format(stockTicker,ALPHAVANTAGE_API_KEY_TWO)
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
