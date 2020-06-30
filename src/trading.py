import requests, json,sys
from config import ALPACA_API_KEY,ALPACA_SECRET_KEY

BASE_URL="https://paper-api.alpaca.markets"
ACCOUNT_URL="{}/v2/account".format(BASE_URL)
ORDER_URL="{}/v2/orders".format(BASE_URL)
HEADER_DATA={"APCA-API-KEY-ID":ALPACA_API_KEY,"APCA-API-SECRET-KEY":ALPACA_SECRET_KEY}


# This function will be used to know the total equity and the buying powers
def account_details():
    result=requests.get(ACCOUNT_URL,headers=HEADER_DATA)
    return json.loads(result.content)
    # Imporatant datas are: 'buying_power' 'cash' and 'portfolio_value'

# This will be used to get the array of all the position history
def stock_positions():
    result=requests.get(ORDER_URL,headers=HEADER_DATA)
    return json.loads(result.content)
    # Returns json data of all positions open, pending or closed

# This will create new market BUY order of passed stock ticker
def buy_stock(symbol,qunatity):
    stockData={
        "symbol":symbol,
        "qty":qunatity,
        "side":"buy",
        "type":"market",
        "time_in_force":"day"
    }
    result=requests.post(ORDER_URL,json=stockData,headers=HEADER_DATA)
    return json.loads(result.content)
    # Returns json data of the position that has been bought

# This will create new market SELL order of passed stock ticker if it exists
def sell_stock(symbol,quantity):
    stockData={
        "symbol":symbol,
        "qty":quantity,
        "side":"sell",
        "type":"market",
        "time_in_force":"day"
    }
    result=requests.post(ORDER_URL,json=stockData,headers=HEADER_DATA)
    return json.loads(result.content)
    # Cannot fill out the provided order is the stock buy is not filled up
    # In such case it will return {'code':40310000,'message':'cannot open a short sell while a long buy order is open'}
    # If you enter a stock that is not in your portfolio the order still gets executed
    # Use stockPosition() method to see if the stock exists before putting selling position

# This will create a new replace order to a buy order already present in portfolio
def replace_order(orderId,newQauantity,newTimeInForce):
    REPLACE_URL="{}/{}".format(ORDER_URL,orderId)
    stockData={
        "qty":newQauantity,
        "time_in_force":newTimeInForce
    }
    result =requests.patch(REPLACE_URL,json=stockData,headers=HEADER_DATA)
    return json.loads(result.content)
    # Function Call Sample: replaceOrder("973964ce-5215-4a5e-9888-c8e9775f7e41","100","day")
    # If the order has not been sent to the exchange then error json is received
    # Example: {'code':40010001,'message':'unable to replace order, order isn't sent to exchange yet'}
    # Else the order is executed, again use stockPosition() function to see all the pending orders
    # Returns order object