#! /usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from pprint import pprint 

def test_app():
	url = "http://localhost:5000/collatz/api/v1.0/3"
	response = requests.get( url )
	pprint( response )
	pprint( response.json()  )

def main():
	test_app()

if __name__ == '__main__':
	main()
