#!/usr/bin/python
from bs4 import BeautifulSoup
import requests

while True:
    choice = input("Do you want games for PS4 or PS5? ")
    if choice == "PS4" or choice == "ps4":
        url = "https://www.public.gr/cat/gaming/games/ps4/?_dyncharset=UTF-8&=undefined&Ns=sku.publicActualPrice|1&Nrpp=790"
        print("Writing PS4 games to csv...")
        break
    elif choice == "PS5" or choice == "ps5":
        url = "https://www.public.gr/cat/gaming/games/ps5/?_dyncharset=UTF-8&=undefined&Nrpp=790&Ns=sku.publicActualPrice|1"
        print("Writing PS5 games to csv...")
        break
    else:
        continue

r = requests.get(url)
html_content = r.text
soup = BeautifulSoup(html_content, 'lxml')
a = soup.findAll("div", {"class": "col-sm-6 col-lg-4"})
filename = "games.csv"


def write_to_excel():
    with open(filename, "w") as f:
        headers = "NAME, PRICE, AVAILABILITY, LINK\n"
        f.write(headers)
        for link in a:
            price = link.div["data-pricerange"]
            availability = link.find("div", {"class": "btn btn-grey btn-as-tag"}).text.strip()
            name = link.find("img")["alt"]
            page = link.find("a", {"class": "product-image product-page-link istile"})["href"]
            address = f"www.public.gr{page}"
            f.write(name + "," + price + "," + availability + "," + address + "\n")


if "ps4" in url:
    write_to_excel()
elif "ps5" in url:
    write_to_excel()
else:
    print("Choose either PS4 or PS5")
print("Done!")
