#!/usr/bin/python
from bs4 import BeautifulSoup
import requests

url = "https://www.public.gr/cat/gaming/games/ps4/?_dyncharset=UTF-8&=undefined&Ns=sku.publicActualPrice|1&Nrpp=790"

r = requests.get(url)
html_content = r.text
soup = BeautifulSoup(html_content, 'lxml')

a = soup.findAll("div", {"class" : "col-sm-6 col-lg-4"})


filename = "games.csv"

with open(filename, "w") as f:
    headers = "NAME, PRICE, AVAILABILITY, LINK\n"
    f.write(headers)
    for link in a:

        price = link.div["data-pricerange"]
        dia8esimothta = link.find("div", {"class":"btn btn-grey btn-as-tag"}).text.strip()
        name = link.find("img")["alt"]
        selida = link.find("a", {"class":"product-image product-page-link istile"})["href"]
        address = f"www.public.gr{selida}"

        print(name)
        print(price)
        print(dia8esimothta)
        print(address)
        f.write(name + "," + price + "," + dia8esimothta + "," + address + "\n")

