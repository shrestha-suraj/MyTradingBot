import requests
import string
from bs4 import BeautifulSoup

def generateStockSymbols():
    file=open("symbols.txt","w")
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
        each=each.replace('.','-').split('-')[0]
        symbols_clean.append(each)
        file.write(each)
        file.write("\n")
    file.close()
    return symbols_clean
