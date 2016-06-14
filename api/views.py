from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

from django.contrib.auth.models import User, Group
from rest_framework import viewsets

import json
import pandas as pandas
import numpy as numpy
from pandas.util.testing import rands

import matplotlib.pyplot as pyplot
import scipy.optimize as sco

# mssql
import pyodbc
import pdb

# Create your views here.
def index(request):

	dsn = 'desarrollo'
	user = 'usr_desa'
	password = 'mifuturo'
	database = 'MFF_SECTORD'

	string_connection = 'DSN=%s;UID=%s;PWD=%s;DATABASE=%s;' % (dsn, user, password, database)
	connection = pyodbc.connect(string_connection)

	response_data = {}
	data_frame_server = pandas.DataFrame()

	symbols = ['AAPL', 'FB', 'GOOG', 'MSFT']
	symbol_quantity = len(symbols)
	for symbol in symbols:
		query = 'EXEC usp_receptaculo_python_test @nemo="' + symbol + '"'
		data_frame_server[symbol] = pandas.read_sql(query, con=connection)

	rets = numpy.log(data_frame_server / data_frame_server.shift(1))

	# TO-DO IMPORT CALL PORTFOLIO_OPTIOMIZATION METHODS
	def statics(weights, rets):
		''' RETURNS PORTFOLIO STATICS

		PARAMETERS
		==========
		weights : array-like
			WEIGHTS FOR DIFFERENT SECURITIES IN PORTFOLIO
		rets :

		RETURNS
		==========
		portfolio_return : float
			EXPECTED PORTFOLIO RETURN

		portfolio_volatility : float
			EXPECTED PORTFOLIO VOLATILITY

		portfolio_return / portfolio_volatility : float
			SHARPE RATIO FOR RF=0
		'''

		weights = numpy.array(weights)
		# GENERAL FORMULA FOR EXPECTED PORTFOLIO RETURN
		portfolio_return = numpy.sum(rets.mean() * weights) * 252
		portfolio_volatility = numpy.sqrt(numpy.dot(weights.T, numpy.dot(rets.cov() * 252, weights)))
		return numpy.array([portfolio_return, portfolio_volatility, portfolio_return / portfolio_volatility])

	def min_fun_sharpe(weights):
		return -statics(weights)[2]

	constraint = ({'type': 'eq', 'fun': lambda x: numpy.sum(x) - 1 })
	bound = tuple((0, 1) for x in range(symbol_quantity))
	# %%time
	optimization = sco.minimize(min_fun_sharpe, symbol_quantity * [1. / symbol_quantity,], method='SLSQP', bounds=bound, constraints=constraint)
	print optimization





	connection.close()
	# response_data['items'] = object_data
	return JsonResponse({})
