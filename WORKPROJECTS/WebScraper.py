import requests
import argparse
import logging

DEFAULT_LOC = 'tx/houston'


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
    r = requests.get('https://www.coldwellbankerhomes.com/{}'.format(args.header))
    if r.status_code == 200:
        logging.info('Successfully connected!')
    else:
        logging.info(r.status_code)

