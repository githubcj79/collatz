#! /usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from pprint import pprint 

def test_app( url ):
	response = requests.get( url )
	pprint( response .status_code )
	pprint( response.json()  )

def main():
	test_app( "http://localhost:5000/collatz/api/v1.0/3" )
	test_app( "http://localhost:5000/collatz/api/v1.0/bad" )

if __name__ == '__main__':
	main()
