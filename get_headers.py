#!/usr/bin/env python3

# Stephen Burke 2020-Dec-7

import requests
from re import search
from pprint import pprint


def tryit():
	url = str(input('\nEnter a url (please specify with http or https):  ')).lower()
	if search("http", url):
		try:
			response = requests.get(url)
			r = str(response.headers)
			fixed = r.replace("\'", "\"")
			print("\n", response, "\n")
			pprint(fixed)
			print("\n")
		except:
		    print("\nError: Well that's awkward\n")
	else:
	    print("Please specify http:// or https://")
	    tryit()
tryit()
   
