#!/usr/bin/env python3

# Stephen Burke 2020-Dec-7

import requests
from pprint import pprint

url = str(input('\nEnter a url (please specify with http or https):  ')).lower()

try:
	response = requests.get(url)
	r = str(response.headers)
	fixed = r.replace("\'", "\"")
	print("\n", response, "\n")
	pprint(fixed)
	print("\n")
except:
    print("\nError: Well that's awkward\n")
   
