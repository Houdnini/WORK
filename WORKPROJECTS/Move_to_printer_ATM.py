#SCRAPED PROJECT

import requests
import logging
import os
import argparse

dir2 = r'C:\Users\Deven\Desktop\Docs_to_print'
url = 'https://aggieprint.tamu.edu/myprintcenter/'

file_list = []


def add_to_printer(link, direct, files):
    r = requests.get(link, auth=('deven.dean26@tamu.edu', 'Bellinger4019'))
    logging.info(r.content)
    logging.info('current status code: {}'.format(r.status_code))
    if r.status_code == 200:
        for file in os.listdir(direct):
            f = os.path.join(direct, file)
            file_list.append(f)
        logging.info('current files within folder: {}'.format(file_list))
        if files in file_list:
            requests.post(link, files=files)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    parser = argparse.ArgumentParser(description='User can choose which file they want added to the printing page for '
                                                 'Texas A&M.')
    parser.add_argument('--select', help='User can select which file they want to be uploaded.', type=str,
                        required=True)
    args = parser.parse_args()
    add_to_printer(url, dir2, args.select)
