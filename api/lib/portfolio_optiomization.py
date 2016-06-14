import numpy as numpy
import pandas as pandas
import numpy as numpy
import scipy.optimize as sco
from pandas.util.testing import rands

import matplotlib.pyplot as pyplot 

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