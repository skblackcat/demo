#!/usr/bin/python
import string
import random
import time
import datetime

DebugMode = False
def getRandomString( numChar=10, characters=string.hexdigits ):
	'''	generate random string from given characters set
	'''
	randomString = ''
	
	for i in xrange( numChar ):
		randomString += random.choice( characters )
		
	return randomString
	
def log( message, onlyDebug=False, dateTimeFormat='%Y-%m-%d %H:%M:%S' ):
	'''	print a message with datetime in given format
	'''
	if DebugMode or not onlyDebug:
		print '[{}]: {}'.format( datetime.datetime.now().strftime( dateTimeFormat ), message )
	
def logTime( func, *args, **kwargs ):
	'''	decorator function to log function time usage
	'''
	log( 'Wrapping function {}'.format( func.__name__ ), onlyDebug=True )
	def wrapperFunc( *args, **kwargs ):
		
		#	get actual function name
		functionName = func.__name__
		
		#	generate random string of this function call, this can be used for separating same function calls
		randomString = getRandomString()
		
		#	remember starting time
		startTime = time.time()
		
		#	start logging before entering to actual function
		log( 'start function: {}[{}] with args {} kwargs {}'.format( functionName, randomString, args, kwargs ), onlyDebug=True )
		
		#	call actual function and don't forget to store return value
		returnValue = func( *args, **kwargs )
		
		#	remember ending time and compute function processing time
		endTime = time.time()		
		totalTime = endTime - startTime
		
		#	log after end calling actual function
		log( 'end function: {}[{}] - total time={}'.format(functionName, randomString, totalTime), onlyDebug=True )
		
		#	this is an important line, return value from actual function
		return returnValue
		
	return wrapperFunc
	
log( 'Initating functions with decorator', onlyDebug=True )
@logTime
def mySleep( second ):
	
	time.sleep( second )

@logTime
def multiply( x, y, decimal=2 ):
	return round( x*y, decimal )

def add( x,y ):
	return x+y

log( 'Starting program..' )
log( 'Multiply result: {}'.format( multiply( 10.53, 1.12345 ) ) )
mySleep( 3 )
log( 'Multiply result: {}'.format( multiply( 10.53, 1.12345, decimal=5 ) ) )
mySleep( 2 )
log( 'End..' )
		
