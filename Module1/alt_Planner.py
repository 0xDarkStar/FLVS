#!/usr/bin/env python3
# The above is a 'shebang line'
# If you are running a Linux/Unix machine like Ubuntu or MacOS
# This line allows it to run as an executable

import time
import math

# Lists for quick and easy access later
# Continents
north = ['north', 'north america', 'North', 'North America', 'North america']
central = ['central', 'central america', 'Central', 'Central America', 'Central america']
south = ['south', 'south america', 'South', 'South America', 'South america']
euro =  ['euro', 'europe', 'eu', 'Euro', 'Europe', 'EU']
middle = ['middle', 'east', 'middle east', 'Middle', 'East', 'Middle East', 'Middle east']
asia = ['asia', 'Asia']
oceania = ['oceania', 'Oceania']
africa = ['africa', 'Africa']
# Countries
usa = ['america', 'usa', 'u.s.a.', 'u.s.a', 'united states', 'united states of america', 'America', 'USA', 'U.S.A.', 'U.S.A', 'United States', 'United States of America', 'United states', 'United states of america']
canada = ['canada', 'canadia', 'Canada', 'Canadia', 'maple syrup']
mex = ['mexico', 'Mexico']

# ⬇️ no need for two new lines, imo ⬇️
print('\nYou are planning on taking a quick vacation for two days to cool down after an exhausting work week.\n')
# time.sleep(3) 

def start():
	continent = input('What continent are you in? ')

	# Instead of having to check for each of the words here
	# You can instead compare the input to the lists
	if continent in north:
		print('success')
	elif continent in central:
		print('success')
		qCountry()
	elif continent in south:
		print('success')
		qCountry()
	elif continent in euro:
		print('success')
		qCountry()
	elif continent in middle:
		print('success')
		qCountry()
	elif continent in asia:
		print('success')
		qCountry()
	elif continent in oceania:
		print('success')
	elif continent in africa:
		print('success')
		qCountry()
	else:
		print("failure\n")
		start()

start()