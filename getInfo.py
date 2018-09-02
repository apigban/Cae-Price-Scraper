#!/usr/bin/env python3.7

import argparse
from datetime import datetime
from pageQueue import redisWrite

def urlCreator(product):

    base_url = 'https://www.carrefouruae.com/mafuae/en/search='

    query_url = base_url + f'{product}'

    #print(query_url)
    return query_url

@redisWrite
def fetchInput():
    """
    Gets parameters from command line arguments and
    passes it to indeed_scraper function in scraper file
    """
    parser = argparse.ArgumentParser(
            description = 'Script that gets keywords to input to carrefour website'
            )
    parser.add_argument(
            '--product',
            '-p',
            type = str,
            help = 'Specific product to fetch the price of',
            required = True)
    parser.add_argument(
            '--user',
            '-u',
            type = str,
            help = 'User that requested the price fetch',
            required = True,
            default = '')
    parser.add_argument(
            '--timestamp',
            '-ts',
            type = str,
            help = 'Time stamp of the request',
            required = False,
            default = datetime.now())

    args = parser.parse_args()
    arg_list = [urlCreator(args.product)]        #init list "arg_list" with url

    for item in vars(args):
        arg_list.append(getattr(args,item))     # for item in namespace, get attribute and append to list "arglist"

    print(arg_list)
    return arg_list
fetchInput()

if __name__ == 'main':
#    urlCreator()
    fetchInput()
