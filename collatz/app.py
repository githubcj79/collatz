#! /usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, jsonify, abort, make_response
import utils

app = Flask(__name__)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Input invalido.'}), 404)

@app.route('/collatz/api/v1.0/<input>', methods=['GET'])
def get_collatz_sequence( input ):
	try:
		n = int( input )
	except Exception as e:
		abort(404)

	return( jsonify( { 'collatz_sequence'  :  utils.collatz_sequence( n )  } ) )


if __name__ == '__main__':
    app.run(debug=True)
