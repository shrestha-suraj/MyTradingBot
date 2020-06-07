import requests
import string
from bs4 import BeautifulSoup

def generateStockSymbols():
    alphabets=list(string.ascii_uppercase)
    symbols=[]
    for alphabet in alphabets:
        url="http://eoddata.com/stocklist/NYSE/{}.htm".format(alphabet)
        resp=requests.get(url)
        site=resp.content
        soup=BeautifulSoup(site,'html.parser')
        table=soup.find('table',{'class':'quotes'})
        for row in table.findAll('tr')[1:]:
            symbols.append(row.findAll('td')[0].text.rstrip())
    symbols_clean=[]
    for each in symbols:
        each=each.replace('.','-')
        symbols_clean.append(each.split('-')[0])
    return symbols_clean
