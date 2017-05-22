#!/usr/bin/python
# Author : Karthikeyan Arulmozhivarman
# Date   : 22 May, 2017
# Descr  : Using OpenWeather APIs

import os 
import sys, getopt
import requests

def get_temparature(argv):

	print 'Weather Report:'

	for city in argv:
		link = 'http://api.openweathermap.org/data/2.5/weather?q='\
			+city+'&appid='+os.environ['APIKEY']
		response = requests.get(link)
		#convert the response to json object
		json_obj = response.json()
		#print response.text
		#check if there exists temparature data in JSON object
		if 'main' not in json_obj or 'temp' not in json_obj['main']:
			print "No temparature data for the city:", city 
			sys.exit()

		country = json_obj['sys']['country']
	        #get the temparature field from JSON object
		tk = float(json_obj['main']['temp'])
	        #convert from kelvin to celsius
		tc = tk -273.15
		print 'City:',city, 'Country:',country,'Temperature: ',\
			tc,'degree celsius'

def usage():
	print ""	
	print("--------------------------------------")	
	print("Usage:")	
	print("--------------------------------------")	
	print("cityname  Cityname should be specified")	
	print("Example:")
        print("python weathermap.py Trichy")	
        print("python weathermap.py NewYork SanJose")	
	print("--------------------------------------")	

def main(argv):

        if len(sys.argv) <= 1:
		print 'ERROR: no arguments found'
		usage()
		sys.exit()

	try:
		opts, args = getopt.getopt(argv,"h",["help"])
	except getopt.GetoptError:
		print 'ERROR: unknown argument'
		usage()
		sys.exit()

	for opt, arg in opts:
		if opt in ("-h","--help"):
			usage()
			sys.exit()

        # calling OpenWeatherMap API inside 
	get_temparature(argv)

if __name__ == "__main__":
   main(sys.argv[1:])
