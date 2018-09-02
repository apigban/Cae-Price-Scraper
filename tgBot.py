#!/usr/bin/env python3.7

import requests
from tg_token import token

url = f'https://api.telegram.org/bot{token}/'

print(url)
