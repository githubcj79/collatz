#! /usr/bin/env python
# -*- coding: utf-8 -*-

def collatz( n ):
	''' Esta función asume que recibe un número natural.'''

	if not n % 2: # even
		return n // 2 
	else: # odd
		return 3 * n + 1
	
def collatz_sequence( input ):
	'''
	Esta función espera un número natural,
	si lo es retorna un string con la secuencia collatz de ese número,
	si no lo es retorna "Input inválido.".
	'''
	try:
		n = int( input )
	except Exception as e:
		return "Input invalido."

	list_ = []
	while not n == 1:
		list_.append( str(n) )
		n = collatz( n )
	list_.append( str(n) )

	return ' ,'.join( list_ ) 
