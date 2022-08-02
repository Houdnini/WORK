import requests
import argparse
import logging
import pandas
from bs4 import BeautifulSoup

DEFAULT_LOC = 'tx/houston'
url = r'https://www.coldwellbankerhomes.com'


def scrapper(r):
    l = []
    c = r.content
    soup = BeautifulSoup(c, 'html.parser')
    all = soup.find_all('div', {'class': 'property-snapshot-psr-panel'})
    for i in range(0, len(all)):
        d = {}
        try:
            d['street'] = all[i].find('span', {'class': 'street-address'}).text
        except:
            pass
        try:
            d['zip'] = all[i].find('span', {'class': 'city-st-zip city-zip-space'}).text
        except:
            pass
        try:
            d['price'] = all[i].find('div', {'class': 'price-normal'}).text
        except:
            pass
        try:
            d['beds'] = all[i].find('li', {'class': 'beds'}).find('div').text
        except:
            pass
        try:
            d['total_baths'] = all[i].find('li', {'class': 'total-baths'}).find('div').text
        except:
            pass
        try:
            d['sqrft'] = all[i].find('li', {'class': 'sq.-ft.'}).text
        except:
            pass
        try:
            d['garage'] = all[i].find('li', {'class': 'car-garage'}).find('div').text
        except:
            pass
        l.append(d)
    return l


def creation_of_table(data):
    df = pandas.DataFrame(data)
    logging.info(df)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    parser = argparse.ArgumentParser(description='User can input what url header as to where it wants the program to '
                                                 'search for houses')
    parser.add_argument('--header', help='User can enter a header for the program to search through', type=str,
                        required=False)
    args = parser.parse_args()
    assert args.header is None or isinstance(args.header, str)
    if args.header:
        pass
    else:
        args.header = DEFAULT_LOC
    r = requests.get('{}/{}'.format(url, args.header))
    c = r.content
    soup = BeautifulSoup(c, 'html.parser')
    current_page = soup.find('a', {'class': 'disabled'}).text
    while True:
        new_web = requests.get('{}/{}/?sortId={}'.format(url, args.header, current_page))
        if r.status_code == 200:
            logging.info('Successfully connected!')
            creation_of_table(scrapper(new_web))
        else:
            logging.info(r.status_code)
            break
        current_page = int(current_page) + 1
        if current_page > 3:
            break
        str(current_page)
