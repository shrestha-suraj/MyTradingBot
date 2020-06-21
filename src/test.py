import requests
import json

url="https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=TSLA&interval=1min&apikey=MON2MJSTOJN7HI6X"
#This returns me the json file of high and lows for the data for the week
result=requests.get(url)
result=json.loads(result.content)["Time Series (1min)"]
print(result["2020-06-19 16:00:00"])
# Above statement prints the below statement
# {'1. open': '1000.1100', '2. high': '1000.9590', '3. low': '999.7800', '4. close': '1000.5700', '5. volume': '78787'}