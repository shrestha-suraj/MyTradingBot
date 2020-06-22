import threading,sys
sys.path.append('./src')
from trading import *
from stockdata import *

# This function is responsible to run a threading function every 15 seconds or as per user set
def set_interval(my_function,interval):
    def function_wrapper():
        set_interval(my_function,interval)
        my_function()
    t=threading.Timer(interval,function_wrapper)
    t.start()
    return t

# This is the main function that will carry out all the processes
def start_module(stocks):
    all_stocks=[]
    all_prices=[]
    for stock in stocks:
        try:
            all_prices.append(float(stockData(stock)['1. open']))
            all_stocks.append(stock)
        except:
            print("Stock not found.")
    print(all_stocks)
    print(all_prices)
    t=threading.Timer(60.00,start_module,args=(stocks,))
    t.start()

def main():
    # This variable holds my buying power
    buying_power=float(accountDetails()['buying_power'])
    each_buying_power=buying_power/5
    # Here I will need the five stocks that I will be targeting
    stocks=top_gainers()
    start_module(stocks)

main()