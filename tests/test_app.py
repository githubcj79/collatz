#! /usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from pprint import pprint 


# try:
# 	n = int( input )
# except Exception as e:
# 	abort(404)


def test_app( url ):
	try:
		response = requests.get( url )
		pprint( response .status_code )
		pprint( response.json()  )
	except Exception as e:
		print ("Requests fallo.\n", e)


def main():
	test_app( "http://localhost:5000/collatz/api/v1.0/3" )
	test_app( "http://localhost:5000/collatz/api/v1.0/bad" )

if __name__ == '__main__':
	main()
