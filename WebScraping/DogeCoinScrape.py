from bs4 import BeautifulSoup
import requests, re

data = requests.get("https://finance.yahoo.com/quote/DOGE-USD/").content
soup = BeautifulSoup(data, 'lxml')
span = soup.find("span", {"class":"Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)"})
price = span.text

span = soup.find("h1", {"class":"D(ib) Fz(18px)"})
name = span.text
print("The item %s has a price of %s" % (name, price))