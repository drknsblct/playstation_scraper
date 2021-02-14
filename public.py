#!/usr/bin/python
from bs4 import BeautifulSoup
import requests


def write_to_excel():
    with open(filename, 'w') as f:
        headers = 'NAME, PRICE, AVAILABILITY, LINK\n'
        f.write(headers)
        for link in a:
            price = link.div['data-pricerange']
            availability = link.find('div', {'class': 'btn btn-grey btn-as-tag'}).text.strip()
            name = link.find('img')['alt']
            page = link.find('a', {'class': 'product-image product-page-link istile'})['href']
            address = f'www.public.gr{page}'
            f.write(name + ',' + price + ',' + availability + ',' + address + '\n')


if __name__ == '__main__':
    while True:
        choice = input('List of games for PS4 or PS5? ')
        if choice.strip().lower() == 'ps4':
            url = 'https://www.public.gr/cat/gaming/games/ps4/?_dyncharset=UTF-8&=undefined&Ns=sku.publicActualPrice|1&Nrpp=790'
            filename = 'ps4_games.csv'
            print('Writing PS4 games to csv...')
            break
        elif choice.strip().lower() == 'ps5':
            url = 'https://www.public.gr/cat/gaming/games/ps5/?_dyncharset=UTF-8&=undefined&Nrpp=790&Ns=sku.publicActualPrice|1'
            filename = 'ps5_games.csv'
            print('Writing PS5 games to csv...')
            break
        else:
            print('Choose either PS4 or PS5!\n')
            continue

    r = requests.get(url)
    html_content = r.text
    soup = BeautifulSoup(html_content, 'lxml')
    a = soup.findAll('div', {'class': 'col-sm-6 col-lg-4'})

    write_to_excel()
    print('Done')
