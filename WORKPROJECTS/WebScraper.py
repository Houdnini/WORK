import requests
import argparse
import logging


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    parser = argparse.ArgumentParser(description='User can input what url header as to where it wants the program to '
                                                 'search for houses')
    parser.add_argument('--header', help='User can enter a header for the program to search through', type=str,
                        required=False)
    args = parser.parse_args()
    r = requests.get('https://www.coldwellbankerhomes.com/{}'.format(args.header))
    if r.status_code == 200:
        logging.info('Successfully connected!')
    else:
        logging.info(r.status_code)

