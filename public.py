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
    urls = [
        'https://www.public.gr/cat/gaming/games/ps4/?_dyncharset=UTF-8&=undefined&Ns=sku.publicActualPrice|1&Nrpp=790',
        'https://www.public.gr/cat/gaming/games/ps5/?_dyncharset=UTF-8&=undefined&Nrpp=790&Ns=sku.publicActualPrice|1']

    csv_filenames = ['ps4_games.csv', 'ps5_games.csv']

    while True:
        choice = input('List of games for [PS4], [PS5] or [both]? ')
        if choice.strip().lower() == 'ps4':
            url = urls[0]
            filename = csv_filenames[0]
            print('Writing PS4 games to csv...')
            break
        elif choice.strip().lower() == 'ps5':
            url = urls[0]
            filename = csv_filenames[1]
            print('Writing PS5 games to csv...')
            break
        elif choice.strip().lower() == 'both':
            for i in range(len(urls)):
                url = urls[i]
                filename = csv_filenames[i]
                print('Writing Playstation games to csv...')
                r = requests.get(url)
                html_content = r.text
                soup = BeautifulSoup(html_content, 'lxml')
                a = soup.findAll('div', {'class': 'col-sm-6 col-lg-4'})
                write_to_excel()
            print('Done')
            break
        else:
            print('Choose either PS4 or PS5!\n')
            continue

    if choice != 'both':
        r = requests.get(url)
        html_content = r.text
        soup = BeautifulSoup(html_content, 'lxml')
        a = soup.findAll('div', {'class': 'col-sm-6 col-lg-4'})

        write_to_excel()
        print('Done')
