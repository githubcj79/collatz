#! /usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
from collatz import utils

@pytest.mark.parametrize(
  "n,expected",
  [ 
  	(11, '11 ,34 ,17 ,52 ,26 ,13 ,40 ,20 ,10 ,5 ,16 ,8 ,4 ,2 ,1'), 
  	(3, '3 ,10 ,5 ,16 ,8 ,4 ,2 ,1'), 
  	('bad' , 'Input inválido.'), 
  ])
def test_collatz_sequence( n, expected ):
	assert utils.collatz_sequence( n ) == expected
