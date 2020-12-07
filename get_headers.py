#!/usr/bin/env python3

# Stephen Burke 2020-Dec-7

import requests

try:
    url = str(input('Enter a url (please specify with http or https):  ')).lower()
    response = requests.get(url)
    print("\n", url, "\n")
    print(response, "\n")
    print(response.headers, "\n")
except:
    print("Error")
   
