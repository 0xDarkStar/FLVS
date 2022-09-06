'''
Meant to calculate cost of: 
	A vacation for two days and one night
	User's (restricted) preference of foods
	Attractions, tours, and/or rides the user might go on
'''

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
atlantic = ['Atlantic', 'atlantic', 'Atlantis', 'atlantis']
space = ['Space', 'space', '']
# Countries
usa = ['america', 'usa', 'u.s.a.', 'u.s.a', 'united states', 'united states of america', 'America', 'USA', 'U.S.A.', 'U.S.A', 'United States', 'United States of America', 'United states', 'United states of america']
canada = ['canada', 'canadia', 'Canada', 'Canadia', 'maple syrup']
mex = ['mexico', 'Mexico']

def main():
	
	print("\n\nYou're planning on taking a vacation for two days to cool down after an exhausting week at work.\n")
	time.sleep(2)
	destination = input("Where do you want to go? (North America, Central America, South America, Europe, Asia, etc.) ")
	destination_length = len(destination)
	destination = destination.replace("!","")
	destination = destination.replace("?","")  #the "or" condition doesn't work in the .replace for some reason...

	print("") #I couldn't find a way to do this without messing something else up...

	a = 0
	b = 0

	while(destination_length == 0): #They didn't input a Continent
		while(a <= 2):
			print(".", end ="", flush = True)
			time.sleep(1.25)
			a += 1
		print("\n\nYou didn't input a continent")
		time.sleep(1)
		destination = input.float("Where do you want to go? (North America, Central America, South America, Europe, Asia, etc.) ")
		destination_length = len(destination)
		b += 1
		if(b == 2):
			time.sleep(2)
			print("\n\nYou know what, since you aren't taking me seriously, fuck it!")
			time.sleep(2)
			quit() #They didn't input a Continent three times

	a = 0
	b = 0 #resetting the "a" and "b" variable for future use

	if destination in atlantic:
		print("If you really want to swim with the fishes you can just head to a beach and swim away from shore.")
		quit()

	elif destination in north:
		print()

	elif destination in central:
		print()

	elif destination in south:
		print()

	elif destination in euro:
		print()

	elif destination in middle:
		print()

	elif destination in asia:
		print()

	elif destination in oceania:
		print()

	elif destination in africa:
		print()

	elif destination in space:
		print("You can't go to space...")
		time.sleep(2)
		print("If we could go to space, I'd allow it. I'd love to go to space, but we can't. :(")
		time.sleep(2.5)
		print("You're going have to restart the program")
		time.sleep(1.25)
		print("I really wish we could go though....")
		time.sleep(.5)
		quit()
main()

'''
use for copy

destination = input("\nWhich airport is closest to you? ")

'''
