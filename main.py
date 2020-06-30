import threading,sys
import src.trading as trading
import src.stocks as stocks
import config as config


stock_to_watch=stocks.top_five_gainers() # Stores the list of five highest moving stocks
stock_100days_high=[]
stock_100days_low=[]
stock_current_price=[]
buying_power=trading.account_details()
for each_stock in stock_to_watch:
    data=stocks.buy_sell_range(each_stock,config.ALPHAVANTAGE_API_KEY_ONE)
    stock_100days_low.append(data['low'])
    stock_100days_high.append(data['high'])


def main():
    for each_stock in stock_to_watch:
        try:
            stock_current_price.append(stocks.each_minute_data(each_stock))
        except:
            stock_current_price.append(0)

main()
print(stock_to_watch)
print(stock_100days_low)
print(stock_100days_high)
print(stock_current_price)





# # This is the main function that will carry out all the processes
# def start_module(stock_dict):
#     for stock in stock_dict:
#         try:
#             # current_stock_monitor[stock]=float(stockData(stock)['1. open'])
#             print(stock)
#             current_price=stockdata.stockData('IBM')['1. open']
#             print(current_price)
#         except:
#             print("Stock not found.")
#     # print(current_stock_monitor)
#     # t=threading.Timer(60.00,start_module,args=(stocks,))
#     # t.start()

# def main():
#     # This variable holds my buying power
#     buying_power=float(trading.accountDetails()['buying_power'])
#     print("Your Buying Power is: "+str(buying_power))
#     each_buying_power=buying_power/5
#     # Here I will need the five stocks that I will be targeting
#     stocks=top_gainers()
#     stock_dict={}
#     for stock in stocks:
#         stock_dict[stock]=stock_analysis(stock)
#     print(stock_dict)
#     start_module(stock_dict)


# print(stocks.top_five_gainers())
# This works no issue

# print(stocks.each_minute_data("OPK"))
# This works with no issue

# print(stocks.buy_sell_range("TSLA",config.ALPHAVANTAGE_API_KEY_TWO))
# This works with no issue

# print(trading.account_details())
# This works with no issue. use "buying_power" to know the buying power for the account

# print(trading.buy_stock('TSLA',1))
# This works with no issues

# print(trading.sell_stock('TSLA',1))
# This works with no issue.