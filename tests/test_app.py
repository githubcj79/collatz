#! /usr/bin/env python
# -*- coding: utf-8 -*-

from pprint import pprint
import pytest
import requests

@pytest.mark.parametrize(
  "status_code,url",
  [ 
  	(200, 'http://localhost:5000/collatz/api/v1.0/3'), 
  	(200, 'http://localhost:5000/collatz/api/v1.0/15'), 
  	(404, 'http://localhost:5000/collatz/api/v1.0/bad'), 
  ])
def test_app( status_code, url ):
	response = requests.get( url )
	assert response .status_code == status_code
