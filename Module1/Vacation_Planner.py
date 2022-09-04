'''
Meant to calculate cost of: 
	A vacation for two days and one night
	User's (restricted) preference of foods
	Attractions, tours, and/or rides the user might go on
'''

import time
import math

def main():

	print("\n\nYou're planning on taking a vacation that'll last two days and one night to cool down after working for your tiring job for years.\n")
	time.sleep(3)
	startRegion = input("What region are you in? North America, Central America, South America, Europe, Middle East, Asia, Oceana, or Africa? ")
	startRegion_length = len(startRegion)
	print("") #I couldn't find a way to do this without messing something else up...

	dots = [".", ".", "."]
	a = 0
	b = 0

	while(startRegion_length == 0): #They didn't input a region
		while(a <= 2):
			print("" + dots[a], end ="", flush = True)
			time.sleep(1.25)
			a += 1
		print("\n\nYou didn't input a region")
		time.sleep(1)
		startRegion = input("What region are you in? North America, Central America, South America, Europe, Middle East, Asia, Oceana, or Africa? ")
		startRegion_length = len(startRegion)
		b += 1
		if(b == 2):
			print("\n\nYou know what, since you aren't taking me seriously, fuck it!")
			quit() #They didn't input a region three times

	a = 0
	b = 0 #resetting the "a" and "b" variable for future use


	if 'north' in startRegion or 'North' in startRegion:
		startCountry = input("\nWhich country are you in? Canada or U.S.A.? ")
		if 'canada' in startCountry:
			countryArea = input ("\nWhere are you in the country? East, West, North, South, North East, North West, etc. ")

		elif 'usa' in startCountry or 'U.S.A.' in startCountry:
			countryArea = input ("\nWhere are you in the country? East, West, North, South, North East, North West, etc. ")

		else:
			print("You aren't in either country?")
			time.sleep(2)
			print("You might've gotten the wrong region, let me end the program for you.")
			quit()


	elif 'central' in startRegion or 'Central' in startRegion:
		startCountry = input("\nWhich country are you in? Mexico, Guatemala, Honduras, El Salvador, Nicaragua, Costa Rica, or Panama? ")
		if 'mexico' in startCountry:
			countryArea = input ("\nWhere are you in the country? North or South ")
		elif 'guatemala' in startCountry:
			startCity = input("\n Which city is closest to you? ")
		elif 'honduras' in startCountry:
			startCity = input("\n Which city is closest to you? ")
		elif 'el' in startCountry or 'salvador' in startCountry:
			startCity = input("\n Which city is closest to you? ")
		elif 'nicaragua' in startCountry:
			startCity = input("\n Which city is closest to you? ")
		elif 'costa' in startCountry or 'rica' in startCountry:
			startCity = input("\n Which city is closest to you? ")
		elif 'panama' in startCountry:
			startCity = input("\n Which city is closest to you? ")
		else:
			print("You might've gotten the wrong region, I'll end the program for you")
			quit()

	elif 'south' in startRegion or 'South' in startRegion:
		startCountry = input("\nWhich country are you in? Colombia, Venezuela, Guyana, Surname, French Guiana, Brazil, Ecuador, Peru, Bolivia, Paraguay, Uruguay, Argentina, or Chile? ")

	elif 'europe' in startRegion or 'Europe' in startRegion:
		startCountry = input("\nWhich country are you in? U.K., Ireland, France, Belgium, Netherlands, Germany, Denmark, Spain, Portugal, I think you get the point.... ")

	elif 'middle' in startRegion or 'Middle' in startRegion or 'East' in startRegion or 'east' in startRegion:
		startCountry = input("\nWhich country are you in? ")

	elif 'asia' in startRegion or 'Asia' in startRegion:
		startCountry = input("\nWhich country are you in? ")

	elif 'oceana' in startRegion or 'Oceana' in startRegion:
		startCountry = input("\nWhich country are you in? ")

	elif 'africa' in startRegion or 'Africa' in startRegion:
		startCountry = input("\nWhich country are you in? ")

	else:
		print("How are you nowhere on Earth?")
		time.sleep(2)
		print("Are you an alien!?")
		time.sleep(1.5)
		print("Aliens aren't allowed to use this program!")
		time.sleep(1)
		print("\nPROGRAM SHUTTING DOWN")
		quit()
main()

'''
use for copy

startRegion = input("What region are you in? ")

startCountry = input("\nWhich country are you in? ")

startCity = input("\n Which city is closest to you? ")

startAirport 
'''
